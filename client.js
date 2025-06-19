

const button = document.querySelector("button");

const changeColor = (number) => {
    return Math.floor(Math.random() * (number + 1));
};

button.addEventListener("click", () => {
    const rndCol = `rgb(${changeColor(255)}, ${changeColor(255)}, ${changeColor(255)})`;
    document.body.style.backgroundColor = rndCol;
});













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