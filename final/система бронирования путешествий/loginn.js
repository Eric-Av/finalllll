const firstNameInput = document.getElementById('first_name')
const lastNameInput = document.getElementById('last_name')
const titleInput = document.getElementById('title')
const descriptionInput = document.getElementById('description')
const button = document.getElementById('button')

$.get('https://technium-frontend-intensive.replit.app', function(data) {
  firstNameInput.value = data.first_name
  lastNameInput.value = data.last_name
  titleInput.value = data.title
  descriptionInput.value = data.description
})
// https://technium-frontend-intensive.replit.app

button.addEventListener('click', function() {

  $.post('https://technium-frontend-intensive.replit.app', {
    first_name: firstNameInput.value,
    last_name: lastNameInput.value,
    title: titleInput.value,
    description: descriptionInput.value,
  }, function() {
    alert("Данные сохранены")
  })
})