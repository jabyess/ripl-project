import Highcharts from 'highcharts'
import HighchartsReact from 'highcharts-react-official'
import highchartsmap from 'highcharts/modules/map'
import { useEffect, useState } from 'react'
import axios from 'axios'
import { transformStateData } from '../utils/utils'

const Map = () => {
    const [mapData, setMapData] = useState({})
    const [seriesData, setSeriesData] = useState([])
    let mapOptions = {}
    let chartMin, chartMax

    highchartsmap(Highcharts)

    useEffect(() => {
        const fetchGeoJson = async () => {
            const geojson = await axios.get("https://code.highcharts.com/mapdata/countries/us/us-all.topo.json")
            setMapData(geojson.data)
        }
        const fetchStateData = async () => {
            const stateSummary = await axios.get("http://localhost:8000/api/states")
            const cleanData = transformStateData(stateSummary.data)
            setSeriesData(cleanData)
        }

        fetchGeoJson()
        fetchStateData()
        console.log(chartMin, chartMax)
    }, [])

    mapOptions = {
        title: {
            text: "Test text",
            style: {
                color: "#FFF"
            }
        },
        chart: {
            backgroundColor: "#FFF",
            type: "map",
            map: mapData,
            width: 1024,
            height: 1024,
            border: "#000"

        },
        mapNavigation: {
            enabled: true,
            enableButtons: true
        },
        credits: {
            enabled: false
        },
        colorAxis: {
            min: 198000,
            max: 239000,
        },

        series: [
            {
                name: "States map",
                dataLabels: {
                    enabled: true,
                    color: "#FFFFFF",
                    // format: "{series.name}",
                    style: {
                        textTransform: "uppercase"
                    }
                },
                tooltip: {
                    valuePrefix: "$",
                },
                cursor: "pointer",
                data: seriesData

            }
        ]
    }

    return (
        <div>
            <HighchartsReact
                highcharts={Highcharts}
                constructorType={"mapChart"}
                options={mapOptions}
            />
        </div>
    )
}

export default Map