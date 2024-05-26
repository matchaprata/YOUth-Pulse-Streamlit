import streamlit as st
st.set_page_config(
    page_title='YOUth Pulse!'
) 
import time
from PIL import Image
import streamlit_survey as ss
if 'login_already' not in st.session_state:
    st.session_state['login_already'] = None

st.title(":rainbow[Youth-Pulse]")
# image = Image.open('logo.png')
# st.image(image)

st.write(
    'A one-stop application for you to check out available political events happening in Singapore for youths.'
)

import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing: border-box;}
body {font-family: Verdana, sans-serif;}
.mySlides {display: none;}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.5s;
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .text {font-size: 11px}
}
</style>
</head>
<body>


<div class="slideshow-container">

<div class="mySlides fade">
  <div class="numbertext">1 / 3</div>
  <img src="https://www.reach.gov.sg/images/default-source/reach-images/read/reflectionsofoursingaporeconversation.jpg" style="width:100%">
</div>

<div class="mySlides fade">
  <div class="numbertext">2 / 3</div>
  <img src="https://scontent.fsin10-1.fna.fbcdn.net/v/t31.18172-8/28515147_10160109028175607_5499300446733944713_o.jpg?_nc_cat=100&ccb=1-7&_nc_sid=5f2048&_nc_ohc=wwAwLud8gQwQ7kNvgE1eog9&_nc_ht=scontent.fsin10-1.fna&oh=00_AYC88IlgnwzlT8qslxlHbAcdAmTV1pH1mki_QVRVTOGp6A&oe=6679C52C" style="width:100%">
</div>

<div class="mySlides fade">
  <div class="numbertext">3 / 3</div>
  <img src="https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F758638169%2F1817535950473%2F1%2Foriginal.20240503-082243?w=1000&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C0%2C2160%2C1080&s=27690f3decea5d0b91afa47bbf55111e" style="width:100%">
</div>

</div>
<br>

<div style="text-align:center">
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span> 
</div>

<script>
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 5000); // Change image every 2 seconds
}
</script>

</body>
</html> 

    """,
    height=420,
)   

st.write(
    'Interested to find out more about other available events? Check them out on our Events page!'
)
