/*
 * Element selectors
 */

console.log('******************** getElementById ****************************');

let myTitle = document.getElementById('title');
console.log(myTitle);
myTitle.innerHTML = '<i>Some dummy title</i>'; // innerHTML renders HTML tags
// myTitle.innerText = '<i>Some dummy title</i>';    // innerText displays HTML tags as content

console.log(myTitle.innerHTML); // display the innerHTML


console.log('******************** getElementsByClassName ****************************');
// getElementsByClassName
// returns HTMLCollection
// Similar to an array, having the elements indexed and even have propertis such as .length
// Read more here: https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection

let boxes = document.getElementsByClassName('box');
console.log(boxes);
console.log(boxes[2]);
console.log(boxes.length);

for (let i = 0; i < boxes.length; i++) {
    console.log(boxes[i]);
    
    boxes[i].style.margin = "5px";
    // boxes[i].style.backgroundColor = "skyblue";
}

console.log('******************** getElementsByTagName ****************************');
// getElementsByTagName
// returns HTMLCollection
// Similar to an array, having the elements indexed and even have propertis such as .length
// Read more here: https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection

let divElements = document.getElementsByTagName('div');
console.log(divElements);
console.log(divElements[2]);
console.log(divElements.length);

for (let i = 0; i < divElements.length; i++) {
    console.log(divElements[i]);
    
    divElements[i].style.borderRadius = "50%";
}


console.log('******************** querySelector ****************************');

let section = document.querySelector('main#content section.box');
console.log(section);
section.style.backgroundColor = "orange";


console.log('******************** querySelectorAll ****************************');
// querySelectorAll
// returns NodeList
// Similar to an array, having the elements indexed and even have propertis such as .length
// Read more here: https://developer.mozilla.org/en-US/docs/Web/API/NodeList

divElements = document.querySelectorAll('div.box');
console.log(divElements);



/*
 * Handle element attributes
 */
console.log('******************** HTML attributes ****************************');
let myLink = document.getElementById('link');
console.log(myLink.href); // Displayes the value of the href-attrbute
myLink.href = '###'; // Manipulates the value of the href-attrbute
console.log(myLink.href); // Displayes the value of the href-attrbute

// Another ways of Adding/changing an attribute is with the method "setAttribute(name, value)"
myLink.setAttribute('target', '_blank');

/*
 * Handle events
 * Some events: click | mouseover | keypress
 */
console.log('******************** Handle events ****************************');
myLink = document.getElementById('link');
myLink.addEventListener('click', function(event) {
    // preventDefault prevents the default behavior of the element
    // In this case the prevented default behavior of the link is to open a new window.
    event.preventDefault();
    // myLink.classList.toggle('hide'); // Toggle does the folllowing: IF (.hide exists) {remove it} ELSE {add .hide}

    alert('You just pressed the link');
});


// Example 2
// let thirdCircle = document.querySelectorAll('div.box')[2]
// console.log(thirdCircle);

let thirdCircle = document.querySelector('#content .box:nth-child(3)')
console.log(thirdCircle);
thirdCircle.addEventListener('mouseover', alertOnMouseOver);
function alertOnMouseOver() {
    alert('You just hoovered over the third circle');
}


/*
 * Navigation
 */
console.log('******************** Navigation ****************************');

let main = document.getElementById('content');
console.log(main);
console.log(main.children);     // Array with index
console.log(main.children[2]);  // Third child
console.log(main.firstElementChild);
console.log(main.lastElementChild);
console.log(main.parentNode);
console.log(main.previousElementSibling);
console.log(main.nextElementSibling);

// Target the first circle
main.firstElementChild.innerText = 'First circle';
// Target the link-text in last child
main.lastElementChild.firstElementChild.innerText += ' :)';
// Target the fifth circle, add some text
main.children[4].innerText = 'fifth circle';
// Target the main headline and add a smiley at the end :)
main.previousElementSibling.innerText += ' :)';



/*
 * Add/Create/Delete element
 */
console.log('******************** Add/Create/Delete element ****************************');

main = document.getElementById('content');

for (let i = 1; i <= 5; i++) {
    // Create element
    let newBox = document.createElement("section");
    // Add some text
    newBox.innerText = "Box " + i;
    // Add a class
    newBox.classList.add('box');
    // Add some style
    newBox.style.margin = '5px';
    console.log(newBox);

    newBox.style.backgroundColor = 'lightgreen';

    newBox.addEventListener('click', function() {
        // newBox.remove(); // Removes the element
        
        // this refers to the object newBox
        this.remove(); // Removes the element

        // this.parentNode.remove(); // Removes the parent element
    })

    // Place the new element in the HTML document somewhere :)
    main.appendChild(newBox);
}
