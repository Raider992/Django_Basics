document.querySelector('.col-lg-5').addEventListener('click', e => {
    const type = e.target.getAttribute('data-el-type');
    switch (type){
        case 'incQualityButton':
            handleIncQuantityButton(e);
            break
        case 'decQualityButton':
            handleDecQuantityButton(e);
            break
        case 'clearPositionButton':
            handleClearPositionButton(e);
            break
        case 'clearButton':
            handleClearCartButton(e);
            break
        default:
            break
    }
});
    const handleClearPositionButton = async (e) => {
        e.preventDefault();
        const productId = e.target.getAttribute('data-id');
        const url = '/cart/clear_position/' + productId + '/'

        try {
            const response = await fetch(url);
            const json = await response.json();
            console.log('Success ' + JSON.stringify(json))
        } catch (e) {
            console.log(e)
        }
    };


    const handleClearCartButton = async (e) => {
        e.preventDefault();

        const url = '/cart/clear/';

        try {
            const response = await fetch(url);
            const json = await response.json();
            console.log('Success ' + JSON.stringify(json))
        } catch (e) {
            console.log(e)
        }
    };

    const handleIncQuantityButton = async (e) => {
        e.preventDefault();
        const productId = e.target.getAttribute('data-id');
        console.log(productId)
        const url = '/cart/add_item/' + productId + '/'

        try {
            const response = await fetch(url);
            const json = await response.json();
            console.log('Success ' + JSON.stringify(json))
        } catch (e) {
            console.log(e)
        }
    };

    const handleDecQuantityButton = async (e) => {
        e.preventDefault();
        const productId = e.target.getAttribute('data-id');
        const url = '/cart/remove_item/' + productId + '/'

        try {
            const response = await fetch(url);
            const json = await response.json();
            console.log('Success ' + JSON.stringify(json))
        } catch (e) {
            console.log(e)
        }
    };
