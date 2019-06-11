new Vue({
  el: '#row',
  created() {
    fetch('/api/boards/getitems')
      .then((response) => {
        if(response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok');
      })
      .then((json) => {
        this.posts.push({
          title: json.title
        })
      })
  }
});