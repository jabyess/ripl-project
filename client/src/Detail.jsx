import { formatCurrency, formatNum } from "../utils/utils"

const Detail = ({ stateDetail }) => {
    const { AREA_TITLE, A_MEAN, A_MEDIAN, A_PCT10, A_PCT25, A_PCT75, A_PCT90, TOT_EMP } = stateDetail[0]
    return (
        <div className="detail">
            <h1>Detail for {AREA_TITLE}</h1>
            <table>
                <thead></thead>
                <tbody>
                    <tr>
                        <td>Mean Annual Salary</td>
                        <td>{formatCurrency(A_MEAN)}</td>
                    </tr>
                    <tr>
                        <td>Median Annual Salary</td>
                        <td>{formatCurrency(A_MEDIAN)}</td>
                    </tr>
                    <tr>
                        <td>10th Percentile</td>
                        <td>{formatCurrency(A_PCT10)}</td>
                    </tr>
                    <tr>
                        <td>25th Percentile</td>
                        <td>{formatCurrency(A_PCT25)}</td>
                    </tr>
                    <tr>
                        <td>75th Percentile</td>
                        <td>{formatCurrency(A_PCT75)}</td>
                    </tr>
                    <tr>
                        <td>90th Percentile</td>
                        <td>{formatCurrency(A_PCT90)}</td>
                    </tr>
                    <tr>
                        <td>Total Employment</td>
                        <td>{formatNum(TOT_EMP)}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    )

}

export default Detail;