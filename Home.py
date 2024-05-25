import streamlit as st
st.set_page_config(
    page_title='YOUth Pulse!'
) 
import time
from PIL import Image
import streamlit_survey as ss

image = Image.open('logo.png')
st.image(image)

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
  <img src="https://static1.straitstimes.com.sg/s3fs-public/styles/large30x20/public/articles/2024/05/02/sgyouth0205.jpg?VersionId=lf8E5LcgW.ORJgWD6Ijhpu1tRZ2d_uUA&itok=xnSXpDRW" style="width:100%">
</div>

<div class="mySlides fade">
  <div class="numbertext">2 / 3</div>
  <img src="https://static1.straitstimes.com.sg/s3fs-public/styles/large30x20/public/articles/2024/03/28/NYC_Youth%20Panels%202_main.JPG?VersionId=porenv70EdCtkb_GQVMprUUfTjOH6Ruu&itok=Kf2zGiiD" style="width:100%">
</div>

<div class="mySlides fade">
  <div class="numbertext">3 / 3</div>
  <img src="https://onecms-res.cloudinary.com/image/upload/s--FpRnaEow--/c_fill,g_auto,h_468,w_830/fl_relative,g_south_east,l_one-cms:core:watermark:reuters,w_0.1/f_auto,q_auto/v1/one-cms/core/2023-03-02t061307z_1_lynxmpej2106a_rtroptp_3_singapore-economy-budget.jpg?itok=cj5RrKdN" style="width:100%">
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
    height=600,
)   

            

        
