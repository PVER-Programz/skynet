let userBalances = {};
let totalBetAmount = 0;

function executeCommand() {
    const input = document.getElementById('commandInput').value.trim();
    const parts = input.split(' ');
    const command = parts[0];
    const params = parts.slice(1);
    
    switch (command) {
        case 'reset_bid':
            reset_bid(...params.map(param => parseInt(param)));
            break;
        case 'add':
            addpoint(...params.map(param => parseInt(param)));
            break;
        case 'sub':
            subpoint(...params.map(param => parseInt(param)));
            break;
        case 'setamt':
            setamt(...params.map(param => parseInt(param)));
            break;
        case 'bet':
            bet(...params.map(param => parseInt(param)));
            break;
        case 'betwon':
            betwon(...params.map(param => parseInt(param)));
            break;
        case 'checkbal':
            console.log(checkbal(...params.map(param => parseInt(param))));
            break;
        case 'checkall':
            console.log(checkall());
            break;
        case 'checkbet':
            console.log(checkbet());
            break;
        case 'refree':
            console.log(refree());
            break;
        default:
            console.log('Invalid command');
    }
    
    document.getElementById('commandInput').value = '';
}

function reset_bid(noofusers, inimon) {
    userBalances = {};
    totalBetAmount = 0;
    const initialMoney = inimon;
    for (let i = 1; i <= noofusers; i++) {
        userBalances[`user${i}`] = initialMoney;
    }
    updateProfiles();
}

function addpoint(userno, amt) {
    if (userBalances.hasOwnProperty(`user${userno}`)) {
        userBalances[`user${userno}`] += amt;
    } else {
        console.error(`User ${userno} does not exist. Cannot add balance.`);
    }
    updateProfiles();
}

function subpoint(userno, amt) {
    if (userBalances.hasOwnProperty(`user${userno}`)) {
        userBalances[`user${userno}`] -= amt;
    } else {
        console.error(`User ${userno} does not exist. Cannot subtract balance.`);
    }
    updateProfiles();
}

function add(userno) {
    const inputAmount = parseInt(document.getElementById(`amountInput${userno}`).value);
    if (!isNaN(inputAmount) && inputAmount > 0) {
        userBalances[`user${userno}`] += inputAmount;
        updateProfiles();
    } else {
        console.error('Invalid input amount. Please enter a valid positive number.');
    }
}

function sub(userno) {
    const inputAmount = parseInt(document.getElementById(`amountInput${userno}`).value);
    if (!isNaN(inputAmount) && inputAmount > 0) {
        if (userBalances[`user${userno}`] >= inputAmount) {
            userBalances[`user${userno}`] -= inputAmount;
            updateProfiles();
        } else {
            console.error('Insufficient balance. Cannot subtract more than available balance.');
        }
    } else {
        console.error('Invalid input amount. Please enter a valid positive number.');
    }
}


function setamt(userno, amt) {
    if (userBalances.hasOwnProperty(`user${userno}`)) {
        userBalances[`user${userno}`] = amt;
    } else {
        console.error(`User ${userno} does not exist. Cannot set balance.`);
    }
    updateProfiles();
}

function bet(amt) {
    const userCount = Object.keys(userBalances).length;
    for (let i = 1; i <= userCount; i++) {
        sub(i, amt);
    }
    totalBetAmount += amt * userCount;
    updateProfiles()
}

function betwon(userno) {
    if (userBalances.hasOwnProperty(`user${userno}`)) {
        add(userno, checkbet());
        totalBetAmount = 0;
    } else {
        console.error(`User ${userno} does not exist. Cannot process bet won.`);
    }
    updateProfiles();
}

function checkall() {
    return userBalances;
}

function checkbet() {
    return totalBetAmount;
}

function refree() {
    const userCount = Object.keys(userBalances).length;
    let refPocket = 0;
    for (let i = 1; i <= userCount; i++) {
        refPocket += checkbal(i);
    }
    refPocket += totalBetAmount;
    const supposedValue = userCount * userBalances[`user${1}`]; // Assuming all users have the same initial balance
    if (supposedValue === refPocket) {
        return true;
    } else {
        console.error(`Refree check failed. RefPocket: ${refPocket}, SupposedValue: ${supposedValue}`);
        return false;
    }
}

function addBet() {
    const betAmount = parseInt(document.getElementById('betAmount').value);
    if (!isNaN(betAmount) && betAmount > 0) {
        bet(betAmount); // Call the bet function with the entered amount
        console.log(`Bet amount of ${betAmount} added successfully.`);
    } else {
        console.error('Invalid bet amount. Please enter a valid positive number.');
    }
}

function updateProfiles() {
    const userCount = Object.keys(userBalances).length;
    let profileHTML = '';
    for (let i = 1; i <= userCount; i++) {
        profileHTML += `
            <div class="profile">
                <div class="userInfo">User ${i}: ${userBalances[`user${i}`]}</div>
                <button onclick="wonBet(${i})">Won Bet</button>
                <input type="number" id="amountInput${i}" placeholder="Enter amount">
                <button onclick="add(${i})">+</button>
                <button onclick="sub(${i})">-</button>
            </div>
        `;
    }
    document.getElementById('userProfiles').innerHTML = profileHTML;
    document.getElementById('totalBetAmount').textContent = totalBetAmount; // Update total bet amount
}

document.getElementById('commandInput').addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        executeCommand();
    }
});


function wonBet(userno) {
    if (userBalances.hasOwnProperty(`user${userno}`)) {
        const winnings = checkbet();
        add(userno, winnings);
        totalBetAmount = 0;
    } else {
        console.error(`User ${userno} does not exist. Cannot process bet won.`);
    }
    updateProfiles();
}

reset_bid(4, 10000); // Call to reset_bid with parameters 4 and 10000 on page load
