console.log('hello 3')

var updateBtns = document.getElementsByClassName('card')
console.log(updateBtns)


for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'action:', action);
        console.log('productId:', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOder(productId, action)
        }
    })
}
  
function updateUserOder(productId, action){
    console.log('User logged in')

    var url = '/rent/update_item/'

    fetch(url, {
        method: 'post',
        headers: {
          "Content-Type":"application/json",
          "X-CSRFToken":csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
      })
      .then((response) =>{
          return response.json()
      })
      .then((data) =>{
        console.log('data:', data);
      })
    }