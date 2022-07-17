from buskita.api import BuskitaApi
import datetime
import asyncio



japan_timezone = datetime.timezone(
	datetime.timedelta(hours=9), 
	name='Japan'
)



buskita_api = BuskitaApi()


async def get_incomings(departure_busstop: int=681, arrival_busstop: int=391) -> list:
	incomings = []

	now_time = datetime.datetime.now(japan_timezone)
	# now_time = datetime.datetime.strptime('2022/07/18 07:13'+'+0900', '%Y/%m/%d %H:%M%z')

	search_results = buskita_api.search_routes(
			target_time=now_time.strftime('%Y/%m/%d %H:%M'),
			# target_time='2022/07/18 07:13',
			departure_busstop=departure_busstop,
			arrival_busstop=arrival_busstop
	)

	for bus in search_results["result"]:
		route_name		 = bus["routes"][0]["name"]

		route_status	   = bus["routes"][0]["status"]
		delay			  = bus["routes"][0]["delay"]

		start_time		 = datetime.datetime.strptime(bus["startDateTime"]+'+0900', '%Y/%m/%d %H:%M%z')
		str_start_time	 = start_time.strftime('%H:%M')

		remaining_time	 = start_time - now_time
		int_remaining_time = int(remaining_time.total_seconds()/60)


		list_route_name = route_name.split()
		route_name = r" ".join(list_route_name[:2])

		int_type = list_route_name[0][0]
		str_type = list_route_name[1]


		try:
			destination = list_route_name[3]
		except IndexError:
			destination = f"約{int_remaining_time}分で到着"
		finally:
			if (int_remaining_time <= 1) and (not int_remaining_time < 0):
				destination = f"まもなくバスがまいります"
			else:
				destination = f"約{int_remaining_time}分で到着"

		if delay:
			delay = f"遅れ約{delay}分"
		else:
			delay = 0

		incomings.append(
			{
				'int_type': int_type,
				'str_type': str_type,
				'time': str_start_time,
				'delay': delay,
				'destination': destination
			}
		)

	if not incomings:
		incomings.append(
			{
				'int_type': "",
				'str_type': "本日の運行は終了しました。",
				'time': "",
				'delay': 0,
				'destination': "運行終了"
			}
		)
		
	return incomings