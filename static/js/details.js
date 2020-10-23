var prdtDtls = document.getElementsByClassName('detail-view')

if ( i = prdtDtls) {
	prdtDtls[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)

		console.log('USER:', user)
		if (user == 'AnonymousUser'){
			console.log('User is not authenticated')
			
		}else{
			detailsProduct(productId, action)
		}

	})
}

function detailsProduct(productId,action){
    console.log('User is authenticated, sending data.....')

        var url='/detail_view/'

        fetch(url,{
            method:'GET',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken
            },
            body:JSON.stringify({'productId':productId, 'action':action})
        })

        .then((response)=>{
            return response.json();
        })

        .then((data)=>{
            console.log('Data:',data)
            location.reload()
        })
}