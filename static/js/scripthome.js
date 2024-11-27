const productContainers = [...document.querySelectorAll('.product-container')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];

productContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})


document.addEventListener('DOMContentLoaded', function () {
    // Select all elements with the class 'book-title'
    var titleElements = document.querySelectorAll('.book-title');

    // Iterate through the NodeList of elements with class 'book-title'
    titleElements.forEach(function (titleElement) {
        // Add 'mouseover' event listener to each element
        titleElement.addEventListener('mouseover', function () {
            // Set the 'title' attribute to the text content of the element
            this.setAttribute('title', this.textContent);
        });
    });
});


var scrollButton = document.getElementById("scrollButton");

// Fonction de défilement vers le bas
function scrollToBottom() {
    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
    // Cacher le bouton après le clic
    scrollButton.style.display = "none";
}