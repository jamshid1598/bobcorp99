const product = {
    plainBurger: {
        name: 'MATO',
        price: 10000,
        amount: 0,
        calory: 1,
        type: 'm²',
        get sum() {
            return this.amount * this.price
        },
        get kcall() {
            return this.amount * this.calory
        }
    },
    freshBurger: {
        name: 'TEMIR PROFIL',
        price: 20500,
        amount: 0,
        calory: 1,
        type: 'm',
        get sum() {
            return this.amount * this.price
        },
        get kcall() {
            return this.amount * this.calory
        }
    },
    freshCombo: {
        name: 'TAXTA',
        price: 31900,
        amount: 0,
        calory: 1,
        type: 'm³',
        get sum() {
            return this.amount * this.price
        },
        get kcall() {
            return this.amount * this.calory
        }
    },
}

const btnPlusOrMinus = document.querySelectorAll('.main__product-btn'),
    delivery = document.querySelector('.addCart')


for (let i = 0; i < btnPlusOrMinus.length; i++) {
    btnPlusOrMinus[i].addEventListener('click', function () {
        addOrSubtract(this)
    })
}

function addOrSubtract(element) {
    const parent = element.closest('.main__product')
    const parentId = parent.getAttribute('id')
    const elementSymbol = element.getAttribute('data-symbol')
    const output = parent.querySelector('.main__product-num')
    const price = parent.querySelector('.main__product-price span')
    const kcall = parent.querySelector('.main__product-kcall span')

    if (elementSymbol == '+') {
        product[parentId].amount++
    } else if (elementSymbol == '-' && product[parentId].amount > 0) {
        product[parentId].amount--
    }

    output.innerHTML = product[parentId].amount
    price.innerHTML = product[parentId].sum
    kcall.innerHTML = product[parentId].kcall
}

const receipt = document.querySelector('.receipt')
const receiptWindow = document.querySelector('.receipt__window')
const receiptWindowOut = document.querySelector('.receipt__window-out')
const receiptWindowBtn = document.querySelector('.receipt__window-btn')

delivery.addEventListener('click', () => {
    let menu = 'Purchuased: \n'
    totalPrice = 0
    kcall = 0

    for (key in product) {
        for (keyId in product[key]) {
            if (product[key].amount > 0 && keyId == 'amount') {
                menu += `${product[key].amount} ${product[key].type} ${product[key].name} \n`
                totalPrice += product[key].sum
                // kcall += product[key].kcall
            }
        }
    }
    receipt.style.display = 'flex';
    setTimeout(() => {
        receipt.style.opacity = '1';
        receiptWindow.style.top = '0'
    }, 100)

    document.body.style.overflow = 'hidden'

    receiptWindowOut.innerHTML = `${menu}\n\n Total price: ${totalPrice}`
    // \n\nCalory: ${kcall}  ------>put it after menu
})

receiptWindowBtn.addEventListener('click', () => location.reload())


const sana = document.querySelector(".header__timer-extra");
recursion()
function recursion(num = 1, speed = 60) {
    let time = new Date(),
        getDat = time.getDate()

    sana.innerHTML = num

    if (num > (getDat/2)) {
        speed *= 2
    }

    if (num != getDat) {
        setTimeout(() => recursion(++num), speed)
    }
}


// rasm ko'rish uchun
const view = document.querySelector('.view')
const images = document.querySelectorAll('.main__product-info')
const viewClose = document.querySelector('.view__close')
const img = document.querySelector('.view img')

images.forEach((el, index) => {
    el.addEventListener('dblclick', function() {
        view.classList.add('active')
        img.setAttribute('src', `images/product${index + 1}.jpg`)
    })
})

viewClose.addEventListener('click', () => {
    view.classList.remove('active')
})

const edit = document.querySelectorAll('.main__product-edit')


//loader !---------------------------------------------------------------->
let loader = document.querySelector('.loader_bg');

window.addEventListener('load', () =>{
    loader.classList.add('hide');
    setTimeout(() => {
        loader.remove();
    }, 600);
});
