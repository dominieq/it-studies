const request = require("request")
const jsdom = require("jsdom")
const {JSDOM} = jsdom

class Wine {
  constructor(name, price, amount, unit) {
    this.name = name
    this.price = price
    this.amount = amount
    this.original_unit = unit
    if(this.original_unit == "l") {
      this.proportion = price / (amount * 1000)
    } else {
      this.proportion = price / amount
    }   
  }

  show_wine() {
    console.log("\n")
    console.log("Wino: " + this.name)
    console.log("Cena: " + this.price + " zł")
    console.log("Ilość: " + this.amount + " " + this.original_unit)
    
    console.log("Koszt jednego mililitra: " + this.proportion)
  }
}

const url = 'https://alkohol-online.pl/15-wina-czerwone'

request(url, function(error, request, body) {
  const dom = new JSDOM(body)
  const document = dom.window.document

  const items = document.querySelectorAll('.product-container')

  let wines = []

  for(const item of items) {
    let title = item.querySelector('.right-block span a').title

    const amount_pos = title.search(/[0-9]{1,3}/)
    const name = title.slice(0, amount_pos)
    const amount_unit = title.slice(amount_pos)

    const unit_pos = amount_unit.search(/ml|l/)
    const amount = amount_unit.slice(0, unit_pos).trim()
    const unit = amount_unit.slice(unit_pos).replace('.', '')
    let price = item.querySelector('.content_price span').textContent.replace(' zł', '').replace(',', '.').trim()

    wines.push(new Wine(name, parseFloat(price), 
    parseInt(amount), unit))
  }

  wines.sort(function(a, b) {
    if(a.proportion > b.proportion) {
      return 1
    } else if (a.proportion < b.proportion) {
      return -1
    } else {
      return 0
    }
  })
  console.log("\nRanking czerwonych win \nwg. najmniejszego kosztu jednego militra: ")
  wines.forEach(wine => wine.show_wine())
})