const $submitButton = $("#submit-button");
const $word = $("#word");
const $score = $("#score");
const inputs = document.querySelectorAll('input');
const $timer = $("#timer");
const $body = $('body')

let guesses = [];
let score = 0;
let timeLimit = 60;
let gameStatus = true;

//function to append text to page - to be used for {Word}: {Response} eventually
function addGuess(guess){
    let $guesses = $("#guesses");

    let t = `<p>${guess}</p>`;
    $guesses.prepend($(t));
}

async function updateScore(points){
    //add the points to the current score
    score += points
    //check if a high score
    high_score = await checkHighScore(score)
    console.log(`HELLO ${high_score}`)
    $score.empty();

    let t = `<p>Current Score: ${score} | High Score: ${high_score}</p>`

    $score.append($(t));
}

async function checkHighScore(num){
    let response = await axios.get(
        `/api/check-score/${num}`
    );
    console.log("highScore =", response.data["high-score"])
    return response.data["high-score"]
}

//query to see if the word is ok, not a word or not in the board and append the word / response to the page
async function checkWord(){
    let word = $word.val();

    let response = await axios.get(
        `/api/check-word/${word}`
    );
    
    console.log("checkWord resp=", response);

    if (response.data["result"]=="ok"){
        points = word.length
        updateScore(points)
    }

    addGuess(`${word}: ${response.data["result"]}`); 
}

//append word to the page - just checking if appending to the page works here

$submitButton.on("click",function(e){
    e.preventDefault();
    if (gameStatus){
        word = $word.val().toUpperCase();
        if(guesses.includes(word)){
            return
        }
        guesses.push(word)
        checkWord()

    }
    else{
        alert("Time is up!")
    }
    inputs.forEach(input=> input.value="")
});

function countdownDisplay(num){

    $timer.empty();

    let t = `<p>Time Left: ${num} seconds</p>`;
    $timer.append($(t));

};

let seconds = timeLimit;
let secondsId = 0;

function start(){
    $body.toggleClass("active")
    secondsId = setInterval("countdown()",1000)
}

function countdown(){
    if (seconds >=0){
        countdownDisplay(seconds)
        seconds = seconds -1;
    } else{
        $timer.empty();
        let t = `<p>Time's Up!</p>`;
        $timer.append($(t))
        gameStatus = false;
        $body.toggleClass("active")
        clearInterval(secondsId);
    }
}

$body.on("load",start())