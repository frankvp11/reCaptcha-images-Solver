// Select the element that you want to observe
const myElement = document.querySelector('.g-recaptcha');

// Create an IntersectionObserver instance
const observer = new IntersectionObserver(entries => {
  // Check if the element is intersecting with the viewport
  if (entries[0].isIntersecting) {
    console.log('Element is now visible on the screen');
    console.log(entries.values)
  } else {
    console.log('Element is no longer visible on the screen');
  }
});

// Start observing the element
observer.observe(myElement);
