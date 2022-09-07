//Veriables ------------------------------------------------------------
var gamestate = 1;

if (gamestate == 1){draw_start_screen();}

//Main function -------------------------------------------------------- 


//if (gamestate == 2){draw_game();}

//if (gamestate == 3){draw_success_screen();}

//if (gamestate == 4){draw_failure_screen();}


//Get Cursor Function ---------------------------------------------------


const canvas = document.querySelector('#canvas');
const context = canvas.getContext('2d');

const CANVAS_WIDTH = canvas.width = 600;
const CANVAS_HEIGHT = canvas.height = 600;
//dasdfddf
//const playerImage = new Image();
//playerImage.src = "shadow"

//console.log(context)

var startScreenX = 230;
var startScreenY = 240;
var startScreenWidth = 140;
var startScreenHeight = 60;

let mouseDown = 0;  


// --------------------------------------------------------------------
function getCursorPosition(canvas, event) {
    if (gamestate == 1)
    {
    //var gamestate = 1
    const rect = canvas.getBoundingClientRect()
    const x = event.clientX - rect.left 
    const y = event.clientY - rect.top
    if (( x >= startScreenX && x <=  
        (startScreenX + startScreenWidth) && 
        (y >= startScreenY && y <=  (startScreenY + startScreenHeight))))
    {
        console.log("x: " + x + " y: " + y);
        gamestate = 2;


        if (gamestate == 2){
            draw_game();
            console.log("gamestate (in gamestate 2) = " + gamestate);
}
        console.log("gamestate = " + gamestate);
    }
    }
}

console.log("Gamestate is being printed outside the function: " + gamestate);

canvas.addEventListener('mousedown', function(e){
getCursorPosition(canvas,e)
})

//Hello
/*
//Function to get the mouse position
function getMousePos(canvas, event){
    var rect = canvas.get
    return {
        x: event.clientX - rect.left,
        y: event.clientY - rect.top
    };
}
*/
// --------------------------------------------------------------------
canvas.onmousedown = () => {  
  mouseDown = mouseDown + 1;  
  if (mouseDown) {  
    console.log('mouse button down')  
  }  
}  
canvas.onmouseup = () => {  
    mouseDown = mouseDown - 1;
  if (mouseDown) {  
    console.log('mouse button down')  
  }  
}

function draw_start_screen(){

    context.clearRect(0,0,CANVAS_WIDTH,CANVAS_HEIGHT);
    context.fillRect(startScreenX,startScreenY,startScreenWidth,startScreenHeight);
    context.fillStyle = 'rgba(255,0,0,1)';
    requestAnimationFrame(draw_start_screen);
    context.font = "36px Comic Sans MS"; //Can use this font instead:
    context.fillText("START", startScreenX + 9, startScreenY + startScreenHeight - 15)
    context.fillStyle = 'rgba(0,0,0,1)';
};


function draw_game(){
    context.fillStyle = 'rgba(255,0,0,1)'; // Red 
    context.fillRect(10,170,160,60); // Rectangle
    requestAnimationFrame(draw_game); // Draw rectangle live
};

console.log("Gamestate before if gamestate 1 " + gamestate)




/*
function getCursorPosition(canvas, event) {
    const rect = canvas.getBoundingClientRect()
    const x = event.clientX - rect.left 
    const y = event.clientY - rect.top
    console.log("x: " + x + " y: " + y)
}

const canvas = document.querySelector('#canvas');
canvas.addEventListener('mousedown', function(e){
getCursorPosition(canvas,e)
})


//Function to get the mouse position
function getMousePos(canvas, event){
    var rect = canvas.get
    return {
        x: event.clientX - rect.left,
        y: event.clientY - rect.top
    };
}

//Function to check whether a point is inside a rectangle
function isInside(pos,rect){
    return pos.x >rect.x && pos.x < rect.x+rect.width && pos.y < rect.y_rect.height && pos.y > rect.y
} // Maybe make on two lines if function is working

var canvas = document.querySelector('#canvas'); // Gets canvas veriable from HTML
var context = canvas.getContext('2d') // Gets context from canvas 

//The rectangle should have x,y,width,height properties
var startRect = {
    x: 230,
    y: 170,
    width: 140,
    height: 60
}

//Binding the click event on the canvas?
canvas.addEventListener('click', function(event) {
    var mousePos = getMousePos(canvas,event);

    if (isInside(mousePos, rect)) {
        alert('clicked inside rect');
    }else{
        alert('clicked outside rect');
    }
}, false);


// ----------------------------------------------------------------------

function draw_game(){ //Move this function to after failure screen
}

function draw_start_screen() {

    let canvas = document.querySelector('#canvas');

    if (!canvas.getContext){
        return;
    }

    let context = canvas.getContext('2d');

        context.fillStyle = 'rgba(255,0,0,1)';
        context.fillRect(230,170,140,60);

        context.fillStyle = 'rgba(0,0,0,1)'
        context.font = "36px Comic Sans MS"; //Can use this font instead:
        context.fillText("START", 239, 212)
}


function draw_success_screen(){
    let canvas = document.querySelector('#canvas');

    if (!canvas.getContext){
        return;
    }

    const context = canvas.getContext('2d');

    context.fillStyle = 'rgba(0,255,0,0.8)';
    context.fillRect(215,170,170,60);

    context.fillStyle = 'rgba(0,0,0,1)'
    context.font = "36px Comic Sans MS"; //Can use this font instead:
    //freesansbold.ttf
    context.fillText("Success!", 228, 212)
}

function draw_failure_screen(){
    let canvas = document.querySelector('#canvas');

    if (!canvas.getContext){
        return;
    }

    let context = canvas.getContext('2d');

    context.fillStyle = 'rgba(255,0,0,1)';
    context.fillRect(220,170,160,60);

    context.fillStyle = 'rgba(0,0,0,1)'
    context.font = "36px Comic Sans MS"; //Can use this font instead:
    //freesansbold.ttf
    context.fillText("Failure!", 239, 212)
}


//Testing functions -----------------------------------------------------
console.log("HelloWorld")

// ----------------------------------------------------------------------
*/