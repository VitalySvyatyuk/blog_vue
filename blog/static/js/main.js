// delimiters: ['[[', ']]'],
// var example2 = new Vue({
//   delimiters: ['[[', ']]'],
//   el: '#example-2',
//   data: {
//     parentMessage: 'Parent',
//     items: [
//       { message: 'Foo' },
//       { message: 'Bar' }
//     ]
//   }
// });
//
// var example3 = new Vue({
//   delimiters: ['[[', ']]'],
//   el: '#example-3',
//   data: {
//   }
// })

Vue.component('blog-post', {
  props: ['title', 'body'],
  template: `
    <div class="blog-post">
      <h3>{{ title }}</h3>
      <label>{{ body }}</label>
    </div>`
})

new Vue({
  delimiters: ['[[', ']]'],
  el: '#blog-post-demo',
  data: {
    posts: []
  },
  created: function () {
    var vm = this
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(function (response) {
        return response.json()
      })
      .then(function (data) {
        vm.posts = data
      })
  }
})