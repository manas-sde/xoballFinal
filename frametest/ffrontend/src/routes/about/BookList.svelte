<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
  
    export let books = [];
    
    function handleBookClick(book) {
      dispatch('bookClicked', book);
    }
  </script>
  
  <ul>
    {#each books as book}
      <li on:click={() => handleBookClick(book)}>
        <strong>{book.title}</strong> - <em>{book.author}</em>
      </li>
    {/each}
  </ul>
  