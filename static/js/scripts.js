document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('studentForm');
    const studentList = document.getElementById('studentList');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const data = {
            name: formData.get('name'),
            email: formData.get('email'),
            faculty: formData.get('faculty')
        };

        fetch('/students', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(data.message);
                form.reset();
                loadStudents();
            } else if (data.error) {
                alert(data.error);
            }
        })
        .catch(error => console.error('Error:', error));
    });

    function loadStudents() {
        fetch('/students')
        .then(response => response.json())
        .then(students => {
            studentList.innerHTML = '';
            students.forEach(student => {
                const li = document.createElement('li');
                li.textContent = `${student[1]} (${student[2]}) - ${student[3]}`;
                studentList.appendChild(li);
            });
        })
        .catch(error => console.error('Error:', error));
    }

    loadStudents();
});