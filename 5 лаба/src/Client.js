import {Link} from 'react-router-dom'
function Client(props) {
    return (
        <div>
            <ul>
                <li>
                    <Link to="/">Rent</Link>
                </li>
                <li>
                    <Link to="/client">Client</Link>
                </li>
            </ul>
            <h1>Client</h1>
            <ul>
                {props.client.map(el =>
                    <li key={el.id_client}>
                        <b>{el.FIO}</b>
                        <b>{el.birthday}</b>
                        <b>{el.phone}</b>
                        <br/>{el.e_mail}
                    </li>)}
            </ul>
        </div>


    )
}