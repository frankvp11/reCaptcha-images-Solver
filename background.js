chrome.runtime.onInstalled.addListener(() => {
    // Show the extension's icon when an element with the class '.my-element' is detected
    chrome.declarativeContent.onPageChanged.addRules([
      {
        conditions: [
          new chrome.declarativeContent.PageStateMatcher({
            css: ['.g-recaptcha']
          })
        ],
        actions: [new chrome.declarativeContent.ShowPageAction()]
      }
    ]);
  });

