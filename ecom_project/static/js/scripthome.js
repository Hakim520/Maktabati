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


// JavaScript to set full title as tooltip on hover
document.addEventListener('DOMContentLoaded', function() {
    var titleElement = document.getElementById('book-title');
    titleElement.addEventListener('mouseover', function() {
        this.setAttribute('title', this.textContent);
    });
});

