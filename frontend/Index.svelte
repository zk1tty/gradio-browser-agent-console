<svelte:options accessors={true} />

<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { Block, BlockTitle } from "@gradio/atoms";
	import { BaseButton } from "@gradio/button";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import { createEventDispatcher, onMount, tick } from "svelte";

	export let gradio: Gradio<{
		change: never;
		submit: never;
		input: never;
		clear_status: LoadingStatus;
	}>;
	export let label = "Textbox";
	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value = "";
	export let placeholder = "";
	export let show_label: boolean;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus | undefined = undefined;
	export let value_is_output = false;
	export let interactive: boolean;
	export let rtl = false;
	export let root: string;

	let el: HTMLTextAreaElement | HTMLInputElement;
	const container = true;

	// ADDED
	const dispatch = createEventDispatcher();
	// expose functions to Python ↔︎ frontend bridge
	onMount(() => {
		// focus log textarea at start
		(document.getElementById("log") as HTMLTextAreaElement)?.scrollTo(0, 1e6);
	});

	function send(cmd: string) {
		dispatch("change", { event: cmd });   // goes to .preprocess()
	}

	function handle_change(): void {
		gradio.dispatch("change");
		if (!value_is_output) {
			gradio.dispatch("input");
		}
	}

	async function handle_keypress(e: KeyboardEvent): Promise<void> {
		await tick();
		if (e.key === "Enter") {
			e.preventDefault();
			gradio.dispatch("submit");
		}
	}

	$: if (value === null) value = "";

	// When the value changes, dispatch the change event via handle_change()
	// See the docs for an explanation: https://svelte.dev/docs/svelte-components#script-3-$-marks-a-statement-as-reactive
	$: value, handle_change(), send("start");
</script>

<div>
	<!--- ADDED -->
	<div class="flex flex-col gap-2 h-full w-full">
		<div class="flex gap-2">
		  <BaseButton variant="primary"   on:click={() => fire("start")}>Start</BaseButton>
		  <BaseButton variant="negative"  on:click={() => fire("stop")}>Stop</BaseButton>
		  <BaseButton variant="secondary" on:click={() => fire("replay")}>Replay</BaseButton>
		</div>
	  
		<textarea
		  bind:value
		  readonly
		  class="flex-1 bg-black text-green-300 p-2 font-mono text-xs overflow-y-scroll"
		/>
	</div>
</div>

<style>
	label {
		display: block;
		width: 100%;
	}

	input {
		display: block;
		position: relative;
		outline: none !important;
		box-shadow: var(--input-shadow);
		background: var(--input-background-fill);
		padding: var(--input-padding);
		width: 100%;
		color: var(--body-text-color);
		font-weight: var(--input-text-weight);
		font-size: var(--input-text-size);
		line-height: var(--line-sm);
		border: none;
	}
	.container > input {
		border: var(--input-border-width) solid var(--input-border-color);
		border-radius: var(--input-radius);
	}
	input:disabled {
		-webkit-text-fill-color: var(--body-text-color);
		-webkit-opacity: 1;
		opacity: 1;
	}

	input:focus {
		box-shadow: var(--input-shadow-focus);
		border-color: var(--input-border-color-focus);
	}

	input::placeholder {
		color: var(--input-placeholder-color);
	}
</style>
