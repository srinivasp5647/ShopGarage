function addToCart(event) {
    event.preventDefault();
    var pro_id = event.srcElement.dataset.prodid
    console.log('Product id :', pro_id);
    
    console.log('User:', user);
    if (user == 'AnonymousUser'){
        console.log('User is not authenticated')
    }else {
        updateCart(pro_id)
    }
}


function updateCart(pro_id){
    console.log('User is authenticated, sending data..')

    var url = '/addtocart/'

    fetch (url, {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body : JSON.stringify({'productId' : pro_id})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data :', data)
    })
}