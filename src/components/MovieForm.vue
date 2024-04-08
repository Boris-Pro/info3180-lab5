<template>
  <div>
    <h2>Add Movie</h2>
    <form @submit.prevent="saveMovie" id="movieForm">
      <!-- Form fields for title, description, and poster upload -->
      <div class="form-group">
        <label for="title">Movie Title</label>
        <input type="text" name="title" class="form-control" v-model="title" required>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea name="description" class="form-control" v-model="description" required></textarea>
      </div>
      <div class="form-group">
        <label for="poster">Movie Poster</label>
        <input type="file" name="poster" class="form-control-file" accept="image/*" @change="handleFileUpload" required>
      </div>
      <!-- Submit button -->
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const title = ref('');
const description = ref('');
let poster = null;
const csrf_token = ref("");

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then(response => response.json())
    .then(data => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    })
    .catch(error => {
      console.error('Error fetching CSRF token:', error);
    });
}

onMounted(() => {
  getCsrfToken();
});

function saveMovie() {
  const movieForm = document.getElementById('movieForm');
  const formData = new FormData(movieForm);
  
  fetch("/api/v1/movies", {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
    
  })
  .catch(error => {
    console.error('Error:', error);
    
  });
}

function handleFileUpload(event) {
  const file = event.target.files[0];
  if (file) {
    poster = file; 
  }
}
</script>
