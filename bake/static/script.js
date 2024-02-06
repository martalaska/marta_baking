const button = document.getElementById("cake_button");
const piece1 = document.getElementById("piece1");
const piece2 = document.getElementById("piece2");
const piece3 = document.getElementById("piece3");
const piece4 = document.getElementById("piece4");
const piece5 = document.getElementById("piece5");
const piece6 = document.getElementById("piece6");
const piece7 = document.getElementById("piece7");
const piece8 = document.getElementById("piece8");
const flavor_combos = document.getElementById("flavor_combos");

button.addEventListener("click", () => {
    button.disabled = true;
    piece1.classList.add("piece1_out");
    piece2.classList.add("piece2_out");
    piece3.classList.add("piece3_out");
    piece4.classList.add("piece4_out");
    piece5.classList.add("piece5_out");
    piece6.classList.add("piece6_out");
    piece7.classList.add("piece7_out");
    piece8.classList.add("piece8_out");
    document.getElementById("click_here").classList.add("click_here_dis");
    document.getElementById("arr").classList.add("arr_dis");
    //document.getElementById("question").classList.add("question_dis");
    //document.getElementsByTagName("h1")[0].style.opacity = 0;
    document.getElementsByClassName("croissant")[1].style.opacity = 0;
    document.getElementsByClassName("croissant")[0].style.opacity = 0;
    document.getElementsByTagName("h1")[0].classList.add("title_small");
    //setTimeout(() => {
    //    document.getElementsByTagName("h1")[0].style.transition = "none";
    //    document.getElementsByTagName("h1")[0].classList.add("title_small");
    //    document.getElementsByTagName("h1")[0].style.transition = "opacity 1s ease-in";
    //    document.getElementsByTagName("h1")[0].style.opacity = 1;
    //}, 2000)
    //document.getElementsByTagName("h1")[0].classList.add("title_small");
    //document.getElementsByClassName("croissant")[0].classList.add("croissant_small");
    //document.getElementsByClassName("croissant")[1].classList.add("croissant_small");
    //document.getElementById("title").classList.add("title_small");
    flavor_combos.style.opacity = 1;
    document.getElementById("question").style.opacity = 0;
    // setTimeout(() => {
    //     document.getElementsByTagName("h1")[0].classList.add("title_small");
    //     document.getElementsByTagName("h1")[0].style.opacity = 1;
    //     //document.getElementsByClassName("lines").style.opacity = 1;
    // }, 2000)

    setTimeout(() => {
        button.remove()
        //document.getElementsByClassName("croissant")[1].remove();
        //document.getElementsByClassName("croissant")[0].remove();
    }, 3000)
})

// flavor_combos.children[1].style.background = "#eb4034";
// flavor_combos.children[3].style.background = "#ebcd34";
// flavor_combos.children[5].style.background = "#fa9b02";
// flavor_combos.children[7].style.background = "#855803";
// flavor_combos.children[9].style.background = "#f5f3e4";
// flavor_combos.children[11].style.background = "#211601";
// flavor_combos.children[11].style.color = "white";
