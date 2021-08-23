async function get_time(area = "Europe", location = "Moscow") {
        try {
            const response = await axios.get(`http://worldtimeapi.org/api/timezone/${area}/${location}`);
            console.log(response);
            return new Date(Date.parse(response.data.datetime));
        } catch (err) {
            console.error(err)
            return null;
        }
    }