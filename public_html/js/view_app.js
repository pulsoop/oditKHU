var db = require('./db');

var app = new Vue({
  el: '#title', // 어떤 엘리먼트에 적용을 할 지 정합니다
  // data 는 해당 뷰에서 사용할 정보를 지닙니다
  data: {
    title: '뷰에서 가져온 제목'
  }   
});

var app1 = new Vue({
  el: '#writer_text', // 어떤 엘리먼트에 적용을 할 지 정합니다
  // data 는 해당 뷰에서 사용할 정보를 지닙니다
  data: {
    name: '뷰에서 가져온 이름'
  }   
});

var app2 = new Vue({
  el: '#date_text', // 어떤 엘리먼트에 적용을 할 지 정합니다
  // data 는 해당 뷰에서 사용할 정보를 지닙니다
  data: {
    date: '뷰에서 가져온 날짜'
  }   
});

var app3 = new Vue({
  el: '#keyword_text', // 어떤 엘리먼트에 적용을 할 지 정합니다
  // data 는 해당 뷰에서 사용할 정보를 지닙니다
  data: {
    keyword: '뷰에서 가져온 키워드'
  }   
});

var app4 = new Vue({
  el: '#location_text', // 어떤 엘리먼트에 적용을 할 지 정합니다
  // data 는 해당 뷰에서 사용할 정보를 지닙니다
  data: {
    location: '뷰에서 가져온 위치'
  }   
});

var app5 = new Vue({
  el: '#content', // 어떤 엘리먼트에 적용을 할 지 정합니다
  // data 는 해당 뷰에서 사용할 정보를 지닙니다
  data: {
    content: '뷰에서 가져온 내용'
  }   
});