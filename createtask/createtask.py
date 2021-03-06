<h1><strong>Rock Paper Scissors</strong></h1>
<h4 style="color:FireBrick;">Welcome to the Playground!</h4>
<p>Click either Rock, Paper, or Scissors.</p>
<h2 id="message"></h2>
<style>
    input[type=text][width:100%;border:2px solid #aaa;]


</style>
<button class="options" id="rock">Rock</button>
<button class="options" id="paper">Paper</button>
<button class="options" id="scissors">Scissors</button>

<div> Your Score: </div>
<p id="humanScore">0</p>


Computer Score:
<p id="computerScore">0</p>


<script>
var scoreComputer = document.getElementById("computerScore");
var scoreHuman = document.getElementById("humanScore");
var rock = document.getElementById("rock");
var paper = document.getElementById("paper");
var scissors = document.getElementById("scissors");
var message = document.getElementById("message");

    const options = document.querySelectorAll(".options");

    options.forEach((option) => {
        option.addEventListener("click", function () {
            const pInput = this.textContent;

            const cOptions = ["Rock", "Paper", "Scissors"];
            const cInput = cOptions[Math.floor(Math.random() * 3)];

            compareInputs(pInput, cInput);
        });
    });
    function winCheck() {
        if (scoreHuman.innerHTML === '5') {
            rock.style.display = "none"
            paper.style.display = "none"
            scissors.style.display = "none"
            message.innerHTML = "You won " + scoreHuman.innerHTML + " - " + scoreComputer.innerText
            scoreHuman.innerHTML = 0;
            scoreComputer.innerHTML = 0;
        } else if (scoreComputer.innerHTML === '5') {
            rock.style.display = "none"
            paper.style.display = "none"
            scissors.style.display = "none"
            message.innerHTML = "You lost " + scoreHuman.innerHTML + " - " + scoreComputer.innerText
            scoreHuman.innerHTML = 0;
            scoreComputer.innerHTML = 0;
        }
    }
    function compareInputs(pInput, cInput) {
        const currentMatch = `${pInput} vs ${cInput}`;
        // Tie check
        if (pInput === cInput) {
            alert(`${currentMatch} is a Tie`);
            return;
        }

        // Rock
        if (pInput === "Rock") {
            if (cInput === "Scissors") {
                alert(`${currentMatch} = You Win`);
                scoreHuman.innerHTML = parseInt(scoreHuman.innerHTML)+1;
                winCheck()
            } else {
                alert(`${currentMatch} = Computer Wins`);
                scoreComputer.innerHTML = parseInt(scoreComputer.innerHTML)+1;
                winCheck()
            }
        }
        // Paper
        else if (pInput === "Paper") {
            if (cInput === "Rock") {
                alert(`${currentMatch} = You Win`);
                scoreHuman.innerHTML = parseInt(scoreHuman.innerHTML)+1;
                winCheck()
            } else {
                alert(`${currentMatch} = Computer Wins`);
                scoreComputer.innerHTML = parseInt(scoreComputer.innerHTML)+1;
                winCheck()
            }
        }
        // Scissors
        else if (pInput === "Scissors") {
            if (cInput === "Paper") {
                alert(`${currentMatch} = You Win`);
                scoreHuman.innerHTML = parseInt(scoreHuman.innerHTML)+1;
                winCheck()
            } else {
                alert(`${currentMatch} = Computer Wins`);
                scoreComputer.innerHTML = parseInt(scoreComputer.innerHTML)+1;
                winCheck()
            }
        }
    }
</script>
