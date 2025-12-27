# Ex.08 Design of Interactive Image Gallery
## Date:26/12/25

## AIM:
To design a web application for an inteactive image gallery with minimum five images.

## DESIGN STEPS:

### Step 1:
Clone the github repository and create Django admin interface.

### Step 2:
Change settings.py file to allow request from all hosts.

### Step 3:
Use CSS for positioning and styling.

### Step 4:
Write JavaScript program for implementing interactivity.

### Step 5:
Validate the HTML and CSS code.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
~~~
gallery.html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Image Gallery</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

<h1>Image Gallery</h1>

<div class="gallery-container">
    <img id="galleryImage" src="{%static 'images/image1.jpg' %}" alt="Gallery Image">

    <div class="buttons">
        <button onclick="prevImage()">Previous</button>
        <button onclick="nextImage()">Next</button>
    </div>
</div>


<script>
    const images = [
        "{% static 'images/image1.jpg' %}",
        "{% static 'images/image2.jpg' %}",
        "{% static 'images/image3.jpg' %}",
        "{% static 'images/image4.jpg' %}",
        "{% static 'images/image5.jpg' %}"
    ];
</script>

<script src="{% static 'js/script.js' %}"></script>

</body>
</html>

style.css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: #f4f4f4;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Heading */
h1 {
    margin: 20px 0;
    color: #333;
}

/* Gallery Box */
.gallery-container {
    width: 500px;
    background: #ffffff;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 0 12px rgba(0, 0, 0, 0.2);
    text-align: center;
}

/* Image */
.gallery-container img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 6px;
    transition: opacity 0.3s ease-in-out;
}

/* Buttons wrapper */
.buttons {
    margin-top: 15px;
}

/* Buttons */
button {
    padding: 10px 20px;
    font-size: 16px;
    margin: 5px;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: #ffffff;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #0056b3;
}

/* Footer (optional) */
footer {
    margin-top: auto;
    width: 100%;
    background-color: #333;
    color: #ffffff;
    text-align: center;
    padding: 15px 0;
    font-size: 14px;
}

/* Mobile responsive */
@media (max-width: 600px) {
    .gallery-container {
        width: 90%;
    }

    .gallery-container img {
        height: 220px;
    }
}

script.js
let currentIndex = 0;

function showImage() {
    document.getElementById("galleryImage").src = images[currentIndex];
}

function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    showImage();
}

function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    showImage();
}

window.onload = showImage;
~~~

## OUTPUT:
![alt text](<Screenshot (71).png>) ![alt text](<Screenshot (72).png>) ![alt text](<Screenshot (73).png>) ![alt text](<Screenshot (74).png>) ![alt text](<Screenshot (75).png>)
## RESULT:
The program for designing an interactive image gallery using HTML, CSS and JavaScript is executed successfully.
