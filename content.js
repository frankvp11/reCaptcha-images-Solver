// Select the element that you want to observe
const myElement = document.querySelector('.g-recaptcha');


// Create an IntersectionObserver instance
const observer = new IntersectionObserver(entries => {
  // Check if the element is intersecting with the viewport
  if (entries[0].isIntersecting) {
    // we found a recaptcha - go ahead and send the website url to the python
    console.log("we found a recaptcha - go ahead and send the website url to the python")
    response = Request("http://127.0.0.1:5000/send", document.URL);
    document.querySelector('#g-recaptcha-response').value = response;
  } else {
    console.log('Element is no longer visible on the screen');
  }
});

// Start observing the element
observer.observe(myElement);


async function Request(url = '', data = {}, method = 'POST') {
  // Default options are marked with *
  const response = await fetch(url, {
    method: method, // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': "application/json;charset=utf-8",
      "Access-Control-Allow-Origin": true
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  const text = await response.text();
  console.log(text);
  return text;
};

