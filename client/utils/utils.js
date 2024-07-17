

const transformStateData = (stateData) => {
    return stateData.map(s => {
        return {
            value: s.A_MEDIAN,
            "hc-key": "us-"+ s.PRIM_STATE.toLowerCase(),
            name: s.AREA_TITLE,
            jobTitle: s.OCC_TITLE
        }
    })
}

const _USDFormatter = new Intl.NumberFormat('en-US', {
    style: "currency",
    currency: "USD",
    trailingZeroDisplay: "stripIfInteger"
})

const formatCurrency = (num) => {
    return _USDFormatter.format(num)
}

const _numFormatter = new Intl.NumberFormat('en-US')

const formatNum = (num) => {
    return _numFormatter.format(num)
}


export { transformStateData, formatCurrency, formatNum}