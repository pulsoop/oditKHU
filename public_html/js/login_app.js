import Vue from 'vue'
import axios from 'axios'

module.exports = {
  mode: 'production'
}

axios.post('/signin', {
  params: { id: id, password: password }
})
	.then(function(response) {
        if (response.status == 200) {
            console.log(response);
        }
    })
	.catch(function(error) {
        if (error.status == 400) {
            console.log(error);
        }
    });