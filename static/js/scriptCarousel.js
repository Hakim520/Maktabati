const carousel = document.querySelector(".carousel");
const arrowBtns = document.querySelectorAll(".wrapper i");
const wrapper = document.querySelector(".wrapper");

const firstCard = carousel.querySelector(".card");
const firstCardWidth = firstCard.offsetWidth;

console.log(wrapper.scrollLeft)
function isScrolledToMax() {
    // The total scrollable width of the carousel
    console.log(carousel.scrollWidth)
    console.log("client" + carousel.clientWidth)

    const maxScrollLeft = carousel.scrollWidth - carousel.clientWidth ;

    // Check if the current scroll position is equal to the maximum scrollable width
    return carousel.scrollLeft >= maxScrollLeft;
}

// Add event listeners for the arrow buttons to  
// scroll the carousel left and right 
arrowBtns.forEach(btn => {
    btn.addEventListener("click", () => {
        
        if (btn.id === "left") {
            carousel.scrollLeft += -2*firstCardWidth;
            console.log(carousel.scrollLeft)
            if(carousel.scrollLeft <= 800) {
                arrowBtns.item(0).classList.add('hide')
            }
            arrowBtns.item(1).classList.remove('hide')
        }
        else {
            carousel.scrollLeft += 2*firstCardWidth;
            if (isScrolledToMax()) {
                arrowBtns.item(1).classList.add('hide')
            }
            arrowBtns.item(0).classList.remove('hide')
        }
        
    });
}); 
