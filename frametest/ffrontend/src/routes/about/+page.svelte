<!-- <script>
	import BookList from './BookList.svelte';
  
	const books = [
	  { title: 'The Hitchhiker\'s Guide to the Galaxy', author: 'Douglas Adams' },
	  { title: '1984', author: 'George Orwell' },
	  { title: 'Brave New World', author: 'Aldous Huxley' }
	];
  
	function handleBookClicked(event) {
	  console.log(event.detail);
	}
  </script>
  <h1>Hello world!</h1>
  <BookList books={books} on:bookClicked={handleBookClicked} />
   -->


   <script>
	let visible = false;
  </script>
  
  <a on:click={() => visible = !visible}>Click me</a>
  <p style="display: {visible ? 'block' : 'none'};">This is a paragraph.</p>
  
  