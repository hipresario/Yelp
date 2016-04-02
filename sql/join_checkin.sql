select biz_usa.business_id as business_id, city, state, latitude, longitude, "attributes.Price Range", checkins from biz_usa INNER JOIN checkins ON biz_usa.business_id = checkins.business_id;

