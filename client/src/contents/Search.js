import axios from 'axios';
import React from 'react'
import AdminNavbar from '../components/AdminNavbar'

function Search() {
    const [data, setData] = React.useState([]);
    React.useEffect(() => {
        axios.get('http://localhost:3001/getcategories').then(
            function (res) {
                setData(res.data);
            }
        )
    }, [])
    return (
        <div>
            <AdminNavbar />
            <div>
                <div className="condiv">
                    {data.map((item, i) =>{
                        return(
                            <div style={{display: 'flex'}}>
                                {item.stock}
                                {item.price}
                                {item.quantity}
                            </div>
                        )
                    })}
                </div>
            </div>
        </div>
    )
}

export default Search
