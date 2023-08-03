import { writable } from 'svelte/store';

export let videoData = [];
export let videoURL = writable('');
export let displayVideoPage=writable(false);
