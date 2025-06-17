
const getStudents = () => {
    fetch('http://127.0.0.1:8000/api/v1/students')
    .then((response) => response.json())
    .then(data => {
    console.log(data);
    })
    .catch(error =>{
        console.error('Error:', error);
    })
};
getStudents()