
//Variables ----------------------------------------------------------------
const canvas = document.querySelector('#canvas');
const context = canvas.getContext('2d');

const CANVAS_WIDTH = canvas.width = 600;
const CANVAS_HEIGHT = canvas.height = 600;

var startScreenX = 230; //Start screen position info
var startScreenY = 240;
var startScreenWidth = 140;
var startScreenHeight = 60; 

var gameScreenX = 220; // GameScreen position info
var gameScreenY = 220;
var gameScreenWidth = 70;
var gameScreenHeight = 70;
var gameScreenGap = 10;

var red = 'rgba(255,0,0,1)'; // Colors 
var green = 'rgba(0,255,0,1)';
var blue = 'rgba(0,0,255,1)';
var yellow = 'rgba(255,255,0,1)';

var redAlt = 'rgba(200,0,0,1)'; //Alternate colors 
var greenAlt = 'rgba(0,170,0,1)';
var blueAlt = 'rgba(0,0,125,1)';
var yellowAlt = 'rgba(200,190,0,1)';

var randNum //Random number
var moveNumber = 0 //Move number 
var squareClickCheck = false;

var moveArray = [move1 = 0, move2 = 0, move3 = 0, move4 = 0,
move5 = 0, move6 = 0, move7 = 0, move8 = 0];
    
var userMoveNumber = [userMove1 = 0, userMove2 = 0, userMove3 = 0,
userMove4 = 0, userMove5 = 0, userMove6 = 0, userMove7 = 0, userMove8 = 0];

var playMoveDone = [playMove1Done = false, playMove2Done = false, 0,
playMove3Done = false, playMove4Done = false, playMove5Done = false,
playMove6Done = false, playMove7Done = false];


/*
var playMove1Done = false;
var playMove2Done = false;
var playMove3Done = false;
var playMove4Done = false;
var playMove5Done = false;
var playMove6Done = false;
var playMove7Done = false;
*/


//console.log("userMoveArray[0] = " + userMoveArray[0]);

/*
var move1 = 0;
var move2 = 0;
var move3 = 0;
var move4 = 0;
var move5 = 0;
var move6 = 0;
var move7 = 0;
var move8 = 0;
*/

/*
rectColor1a = (175,0,0,0.5) #Rect color1a - Red
rectColor2a = (0,155,0,0.5) #Rect color2a - Green
rectColor3a = (0,0,125,0.5) #Rect color3a - Blue 
rectColor4a = (175,175,0,0.5) #Rect color4a - Yellow
*/

var loopRun = true; //Variable that runs loop everytime it is set to true
var startButtonClicked = false;
var gamestate = 1;


//Main ---------------------------------------------------------------------

start();

// Main functions ----------------------------------------------------------
function draw_start_screen(){
    //Draws the start screen 
    context.clearRect(0,0,CANVAS_WIDTH,CANVAS_HEIGHT);
    context.fillRect(startScreenX,startScreenY,startScreenWidth,startScreenHeight);
    context.fillStyle = 'rgba(255,0,0,1)';
    
    context.font = "36px Comic Sans MS"; //Can use this font instead:
    context.fillText("START", startScreenX + 9, startScreenY + startScreenHeight - 15)
    context.fillStyle = 'rgba(0,0,0,1)';
    //Checks for if start Button is clicked
    if (startButtonClicked) 
    {
        gamestate = 2;
        loopRun = true;

       // console.log("startButtonClicked = " + startButtonClicked);
       // console.log("loopRun = " + loopRun);
       // console.log("gamestate = " + gamestate);

        if (gamestate == 2){
            //console.log("Gamestate = 2 inside the loop!");
            draw_game();
            }
    }
    else
    {
        requestAnimationFrame(draw_start_screen);
        //console.log("loopRun = " + loopRun);
    }
}


function start(){
    if(gamestate == 1){
        draw_start_screen();
    }
}

function draw_game(){ 
    playMove1();
    playMove2();
}

function failureScreen(){
    console.log("Hi");
}

/*
function get_input1(){
    userMove1Check();
}

function userMove1Check(){

}
*/

function playMove1(){
    draw_squares();
    setTimeout(() => {draw_random_square();}, 400);
    setTimeout(() => {draw_squares();}, 1000);
    setTimeout(() => {squareClickCheck = true;},1000);   
}

function playMove2(){
    if (playMoveDone[1])
    {
    draw_squares();
    setTimeout(() => {if(moveArray[1] == 1) {draw_squares_red();}}, 400);
    setTimeout(() => {if(moveArray[1] == 2) {draw_squares_green();}}, 400);
    setTimeout(() => {if(moveArray[1] == 3) {draw_squares_blue();}}, 400);
    setTimeout(() => {if(moveArray[1] == 4) {draw_squares_yellow();}}, 400);
    setTimeout(() => {draw_squares();}, 800);
    setTimeout(() => {draw_random_square();}, 1200);
    setTimeout(() => {draw_squares();}, 1800);
    setTimeout(() => {square1ClickCheck = true;},1800);
    }
    else 
    {
        setTimeout(playMove2, 100);
    }
}


function draw_squares(){
    context.clearRect(0,0,CANVAS_WIDTH,CANVAS_HEIGHT);
    draw_red_rect();
    draw_green_rect();
    draw_blue_rect();
    draw_yellow_rect();
}

function draw_squares_alt(){
    context.clearRect(0,0,CANVAS_WIDTH,CANVAS_HEIGHT);
    draw_red_rect();
    draw_green_rect();
    draw_blue_rect();
    draw_yellow_rect();
}

function draw_squares_red(){
    context.clearRect(0,0,CANVAS_WIDTH,CANVAS_HEIGHT);
    draw_red_rect_alt();
    draw_green_rect();
    draw_blue_rect();
    draw_yellow_rect();
}
function draw_squares_green(){
    context.clearRect(0,0,CANVAS_WIDTH,CANVAS_HEIGHT);
    draw_red_rect();
    draw_green_rect_alt();
    draw_blue_rect();
    draw_yellow_rect();
}

function draw_squares_blue(){
    context.clearRect(0,0,CANVAS_WIDTH,CANVAS_HEIGHT);
    draw_red_rect();
    draw_green_rect();
    draw_blue_rect_alt();
    draw_yellow_rect();
}

function draw_squares_yellow(){
    context.clearRect(0,0,CANVAS_WIDTH,CANVAS_HEIGHT);
    draw_red_rect();
    draw_green_rect();
    draw_blue_rect();
    draw_yellow_rect_alt();
}

function draw_random_square(){
moveNumber++;
randNum = Math.floor((Math.random() * 4) + 1); // Random number
switch(randNum){
    case 1: //Red move
        //console.log("Case 1 worked");
        moveArray[moveNumber] = 1;

        draw_squares_red();
        console.log("Red move worked!")
        break;

    case 2: //Green move
        //console.log("Case 2 worked");
        moveArray[moveNumber] = 2;

        draw_squares_green();
        console.log("Green move worked!")
        break;

    case 3: //Blue move
        //console.log("Case 3 worked");
        moveArray[moveNumber] = 3;
        draw_squares_blue();
        console.log("Blue move worked!")
        break;

    case 4: //Yellow move
        //console.log("Case 4 worked"); 
        moveArray[moveNumber] = 4;

        draw_squares_yellow();
        console.log("Yellow move worked!")
        break;      

    default:
        console.log("Something went wrong!");
}
}

function draw_red_rect(){ 
    context.fillStyle = 'rgba(255,0,0,1)';
    context.fillRect(gameScreenX, gameScreenY, gameScreenWidth, gameScreenHeight);
}
function draw_red_rect_alt(){ 
    context.fillStyle = redAlt;
    context.fillRect(gameScreenX, gameScreenY, gameScreenWidth, gameScreenHeight);
}
function draw_green_rect(){ 
    context.fillStyle = 'rgba(0,255,0,1)';
    context.fillRect(gameScreenX + gameScreenWidth + gameScreenGap,
         gameScreenY, gameScreenWidth, gameScreenHeight);
}
function draw_green_rect_alt(){ 
    context.fillStyle = greenAlt;
    context.fillRect(gameScreenX + gameScreenWidth + gameScreenGap,
         gameScreenY, gameScreenWidth, gameScreenHeight);
}
function draw_blue_rect(){ 
    context.fillStyle = 'rgba(0,0,255,1)';
    context.fillRect(gameScreenX, gameScreenY + gameScreenHeight + 
        gameScreenGap, gameScreenWidth, gameScreenHeight);
}
function draw_blue_rect_alt(){ 
    context.fillStyle = blueAlt;
    context.fillRect(gameScreenX, gameScreenY + gameScreenHeight + 
        gameScreenGap, gameScreenWidth, gameScreenHeight);
}
function draw_yellow_rect(){ 
    context.fillStyle = yellow;
    context.fillRect(gameScreenX + gameScreenWidth + gameScreenGap, 
        gameScreenY + gameScreenHeight + gameScreenGap, gameScreenWidth,
        gameScreenHeight);
}
function draw_yellow_rect_alt(){ 
    context.fillStyle = yellowAlt;
    context.fillRect(gameScreenX + gameScreenWidth + gameScreenGap, 
        gameScreenY + gameScreenHeight + gameScreenGap, gameScreenWidth,
        gameScreenHeight);
}

//EventListenerFunctions ---------------------------------------------------
function getCursorPosition(canvas, event){
    const rect = canvas.getBoundingClientRect()
    const x = event.clientX - rect.left 
    const y = event.clientY - rect.top

    if (gamestate == 1){
        if (( x >= startScreenX && x <=  
            (startScreenX + startScreenWidth) && 
            (y >= startScreenY && y <=  (startScreenY + startScreenHeight))))
        {
            startButtonClicked = true;
            console.log("Start button clicked");
        }
    }
    if ((gamestate == 2) && (squareClickCheck)){
        if (( x >= gameScreenX && x <=  
            (gameScreenX + gameScreenWidth) && 
            (y >= gameScreenY && y <=  (gameScreenY + gameScreenHeight))))
            {
                console.log("Red square clicked ");
                userMoveNumber[moveNumber] = 1;
                console.log("moveNumber = " + moveNumber);
                console.log("userMoveNumber[moveNumber] " + userMoveNumber[moveNumber]);
                console.log("moveArray[moveNumber] " + moveArray[moveNumber]);
                playMoveDone[moveNumber] = true;
                for(let x = 1; x <= moveNumber; x++)
                    {
                    console.log("x =" + x);
                    if (userMoveNumber[x] != moveArray[x])
                        {
                        gamestate = 3;
                        failureScreen();   
                        }
                    }
               // square1ClickCheck = false;                
            }
        if (( x >= gameScreenX + gameScreenGap + gameScreenWidth && x <=  
            (gameScreenX + gameScreenWidth + gameScreenGap + gameScreenWidth) && 
            (y >= gameScreenY && y <=  (gameScreenY + gameScreenHeight))))
            {
                console.log("Green square clicked");
                userMoveNumber[moveNumber] = 2;
                console.log("moveNumber = " + moveNumber);
                console.log("userMoveNumber[moveNumber] " + userMoveNumber[moveNumber]);
                console.log("moveArray[moveNumber] " + moveArray[moveNumber]);
                playMoveDone[moveNumber] = true;
                for(let x = 1; x <= moveNumber; x++)
                    {
                    console.log("x =" + x);
                    if (userMoveNumber[x] != moveArray[x])
                        {
                        gamestate = 3;
                        failureScreen();   
                        }
                    }
               // square1ClickCheck = false;
            }
        if (( x >= gameScreenX && x <=  (gameScreenX + gameScreenWidth) && 
            (y >= gameScreenY  + gameScreenGap + gameScreenHeight && y <=  
            (gameScreenY + gameScreenGap + gameScreenHeight + gameScreenHeight))))
            {
                console.log("Blue square clicked ");
                userMoveNumber[moveNumber] = 3;
                console.log("moveNumber = " + moveNumber);
                console.log("userMoveNumber[moveNumber] " + userMoveNumber[moveNumber]);
                console.log("moveArray[moveNumber] " + moveArray[moveNumber]);
                playMoveDone[moveNumber] = true;
                for (let x = 1; x <= moveNumber; x++)
                    {
                        console.log("x =" + x);
                    if (userMoveNumber[x] != moveArray[x])
                        {
                        gamestate = 3;
                        failureScreen();                   
                        }
                    }
               // square1ClickCheck = false;
            }
        if (( x >= gameScreenX + gameScreenGap + gameScreenWidth && x <=  
            (gameScreenX + gameScreenWidth + gameScreenGap + gameScreenWidth) && 
            (y >= gameScreenY  + gameScreenGap + gameScreenHeight  && y <=
            (gameScreenY + gameScreenGap + gameScreenHeight + gameScreenHeight))))
            {
                console.log("Yellow square clicked");
                userMoveNumber[moveNumber] = 4;
                console.log("moveNumber = " + moveNumber);
                console.log("userMoveNumber[moveNumber] " + userMoveNumber[moveNumber]);
                console.log("moveArray[moveNumber] " + moveArray[moveNumber]);
                playMoveDone[moveNumber] = true;
                for(let x = 1; x <= moveNumber; x++)
                    {
                    console.log("x =" + x);
                    if (userMoveNumber[x] != moveArray[x])
                        {
                        gamestate = 3;
                        failureScreen();    
                        }
                    }
               // square1ClickCheck = false;
            }
    }
    
} 

//EventListeners -----------------------------------------------------------
canvas.addEventListener('mousedown', function(e){
    getCursorPosition(canvas,e)
    
})

