

// const button = document.querySelector("button");
const submitButton = document.getElementById('pokeSearchSubmit')
const pokeForm = document.getElementById("pokeForm")


// const getPokemon = async() => {
//     let reponse = await fetch('https://pokeapi.co/api/v2/pokemon/ditto');
//     let data = await reponse.json();
//     let pokePhoto = data['sprites']['front_default'];
//     let pokeImage = document.createElement('img');
//     pokeImage.src = pokePhoto;
//     pokeImage.id = 'pokePic'
//     pokeInfoDiv = document.getElementById("pokeInfo");
//     pokeInfoDiv.appendChild(pokeImage)
// }




pokeForm.addEventListener("submit", async function(e)  {
    e.preventDefault();

    const form = document.getElementById("pokeForm")

    const formData = new FormData(form);

    const response = await fetch("/submit_data", {
      method: "POST",
      body: formData
    });
    const result = await response.json();
    const otherPokemon = document.getElementById('pokeSearch').value.toLowerCase();
    const otherPokeURL = `https://pokeapi.co/api/v2/pokemon/${otherPokemon}`;
    
    fetch(otherPokeURL)
        .then(reponse => {
         return reponse.json()
        })
        .then(data => {
            let pokeImage = document.createElement('img');
            let otherPokePic = data['sprites']['front_default']
            pokeImage.src = otherPokePic;
            pokeInfoDiv = document.getElementById("pokeInfo");
            pokeInfoDiv.appendChild(pokeImage)

        })

})
// const changeColor = (number) => {
//     return Math.floor(Math.random() * (number + 1));
// };

// button.addEventListener("click", () => {
//     const rndCol = `rgb(${changeColor(255)}, ${changeColor(255)}, ${changeColor(255)})`;
//     document.body.style.backgroundColor = rndCol;
// });


// fetch('url')
//     .then(reponse => {
//         if (!reponse.ok){
//             throw new Error(`HTTP Error: {response.status}`)
//         }
//         return reponse.json()
//     })
//         .then(data => {
//             console.log(data)
//         })
//     .catch(error => {
//         console.error(`Error with data:`, error)
//     })








// const getStudents = () => {
//     fetch('http://127.0.0.1:8000/api/v1/students')
//     .then((response) => response.json())
//     .then(data => {
//     console.log(data);
//     })
//     .catch(error =>{
//         console.error('Error:', error);
//     })
// };
// getStudents()