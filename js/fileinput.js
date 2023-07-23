// Define a global variable to hold the uploaded JSON data
window.uploadedData = [];

document.getElementById('fileInput').addEventListener('change', function(evt) {
  // Get the file from the file input element
  var file = evt.target.files[0];

  // Create a new FileReader instance
  var reader = new FileReader();

  // Define what happens when the file is successfully read
  reader.onload = function(e) {
    // Parse the file contents as JSON and assign it to the uploadedData variable
    window.uploadedData = JSON.parse(e.target.result);
    
    // Call init() after the file has been successfully loaded and parsed
    console.log('File uploaded');
    init();
  };

  // Start reading the file as text
  reader.readAsText(file);
});
