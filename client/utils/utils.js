

const transformStateData = (stateData) => {
    return stateData.map(s => {
        return {
            value: s.A_MEDIAN,
            "hc-key": "us-"+ s.PRIM_STATE.toLowerCase(),
            name: s.AREA_TITLE
        }
    })
}


export { transformStateData }