import Highcharts, { format } from 'highcharts'
import HighchartsReact from 'highcharts-react-official'
import highchartsmap from 'highcharts/modules/map'
import { useEffect, useState } from 'react'
import axios from 'axios'
import Detail from './Detail'
import { transformStateData } from '../utils/utils'
import { formatNum } from '../utils/utils'
import './Map.css'

const Map = () => {
    const [mapData, setMapData] = useState({})
    const [seriesData, setSeriesData] = useState([])
    const [stateDetail, setStateDetail] = useState([])
    let mapOptions = {}

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
    }, [])

    const fetchStateDetail = async (state) => {
        const results = await axios.get(`http://localhost:8000/api/state/${state}`)
        setStateDetail(results.data)

        return results.data
    }

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
            height: 900,
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

        plotOptions: {
            series: {
                events: {
                    click: (e) => {
                        const stateAbbr = e.point.options['hc-key'].substring(3).toUpperCase()
                        fetchStateDetail(stateAbbr)
                    }
                }
            }
        },
        series: [
            {
                name: "States map",
                dataLabels: {
                    enabled: true,
                    color: "#FFFFFF",
                    formatter: function () {
                        return formatNum(this.point.value)
                    },

                },
                tooltip: {
                    valuePrefix: "$",
                    headerFormat: "<span>Highest Median Salary</span><br/>",
                    pointFormat: "<span>{point.jobTitle}: {point.value}</span><br/><span>{point.name}</span>",
                },
                cursor: "pointer",
                data: seriesData,
            }
        ]
    }

    return (
        <>
            <h1 class="title">RIPL BLS Data</h1>
            <div className="map-container">
                <div>
                    <HighchartsReact
                        highcharts={Highcharts}
                        constructorType={"mapChart"}
                        options={mapOptions}
                    />
                </div>
                <div>
                    {stateDetail.length > 0 && <Detail stateDetail={stateDetail} />}
                </div>
            </div>
        </>
    )
}

export default Map