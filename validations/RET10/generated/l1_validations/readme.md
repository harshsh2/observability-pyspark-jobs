

- **search** : All the following sub conditions must pass as per the api requirement

	- **SEARCH_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["search"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["search"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["search"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["search"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["search"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["search"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **SEARCH_PAYMENT** : All the following sub conditions must pass as per the api requirement
	
		- **PAYMENT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition PAYMENT_REQUIRED_TYPE**: $.message.intent.payment['@ondc/org/buyer_app_finder_fee_type'] must be present in the payload
			
			- **condition PAYMENT_REQUIRED_AMOUNT**: $.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount'] must be present in the payload
		
		- **SEARCH_CATEGORY** : All the following sub conditions must pass as per the api requirement
		
			- **condition CATEGORY_REQUIRED_ID**: every element of $.message.intent.category.id must be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Bakery, Cakes & Dairy", "Pet Care", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks", "Gift Voucher"]
			
				> Note: **Condition CATEGORY_REQUIRED_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.category.id must **not** be present in the payload
			
			- **PAYMENT_ENUM** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_ENUM_TYPE**: every element of $.message.intent.payment['@ondc/org/buyer_app_finder_fee_type'] must be in ["percent", "amount"]
				
				- **condition PAYMENT_REGEX_AMOUNT**: all elements of $.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount'] must follow every regex in ["^(\\d*.?\\d{1,2})$"]
		
		- **FULFILMENT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILMENT_ENUM_TYPE**: every element of $.message.intent.fulfillment.type must be in ["Delivery", "Self-Pickup", "Buyer-Delivery"]
			
				> Note: **Condition FULFILMENT_ENUM_TYPE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.fulfillment.type must **not** be present in the payload
			
			- **condition FULFILMENT_REQUIRED_END_LOCATION_GPS**: all elements of $.message.intent.fulfillment.end.location.gps must follow every regex in ["^\\d{2}\\.\\d{4,}\\s*,\\s*\\d{2}\\.\\d{4,}$"]
			
				> Note: **Condition FULFILMENT_REQUIRED_END_LOCATION_GPS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.fulfillment.end.location.gps must **not** be present in the payload
			
			- **condition FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE**: all elements of $.message.intent.fulfillment.end.location.address.area_code must follow every regex in ["^\d{6}$"]
			
				> Note: **Condition FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.fulfillment.end.location.address.area_code must **not** be present in the payload
	
	- **SEARCH_TAGS** : All the following sub conditions must pass as per the api requirement
	
		- **condition SEARCH_TAG_VALID_TAGS**: every element of $.message.intent.tags[*].code must be in ["catalog_inc", "bap_terms", "catalog_full", "bap_features", "bap_promos", "bnp_demand_signal"]
		
			> Note: **Condition SEARCH_TAG_VALID_TAGS** can be skipped if the following conditions are met:
			>
			> - **condition B**: $.message.intent.tags[*].code must **not** be present in the payload
		
		- **TAGS_BNP_FEATURES** : All the following sub conditions must pass as per the api requirement
		
			- **condition TAGS_BNP_FEATURES_PAYLOAD_TYPE_VALID**: every element of $.message.intent.tags[?(@.code=='bap_features')].list[*].code must be in ["001", "002", "003", "004", "005", "006", "007", "008", "0091", "0092", "0093", "0094", "0095", "0096", "0097", "0098", "0099", "00A", "00B", "00C", "00D", "00E", "00F", "010", "011", "012", "013", "014", "015", "016", "017", "018", "019", "01A", "01B", "01C", "01D", "01E", "01F", "020", "021", "022", "023", "024", "025"]
			
				> Note: **Condition TAGS_BNP_FEATURES_PAYLOAD_TYPE_VALID** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='bap_features')].list[*].code must **not** be present in the payload
			
			- **condition TAGS_BNP_FEATURES_PAYLOAD_TYPE**: every element of $.message.intent.tags[?(@.code=='bap_features')].list[*].value must be in ["yes"]
			
				> Note: **Condition TAGS_BNP_FEATURES_PAYLOAD_TYPE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='bap_features')].list[*].value must **not** be present in the payload
		
		- **TAGS_BAP_TERMS** : All the following sub conditions must pass as per the api requirement
		
			- **condition TAGS_BAP_TERMS**: every element of $.message.intent.tags[?(@.code=='bap_terms')].list[*].code must be in ["static_terms", "static_terms_new", "effective_date"]
			
				> Note: **Condition TAGS_BAP_TERMS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='bap_terms')].list[*].code must **not** be present in the payload
			
			- **condition TAGS_BAP_TERMS_EFFECTIVE_DATE**: all elements of $.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='effective_date')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
		
		- **TAGS_CATALOG_FULL** : All the following sub conditions must pass as per the api requirement
		
			- **condition TAGS_CATALOG_FULL_VALID_ENUMS**: every element of $.message.intent.tags[?(@.code=='catalog_full')].list[*].code must be in ["payload_type"]
			
				> Note: **Condition TAGS_CATALOG_FULL_VALID_ENUMS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='catalog_full')].list[*].code must **not** be present in the payload
			
			- **condition TAGS_CATALOG_FULL_PAYLOAD_TYPE**: every element of $.message.intent.tags[?(@.code=='catalog_full')].list[?(@.code=='payload_type')].value must be in ["link", "inline"]
			
				> Note: **Condition TAGS_CATALOG_FULL_PAYLOAD_TYPE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='catalog_full')].list[?(@.code=='payload_type')].value must **not** be present in the payload
		
		- **TAGS_CATALOG_INC** : All the following sub conditions must pass as per the api requirement
		
			- **condition TAGS_CATALOG_INC_VALID_ENUMS**: every element of $.message.intent.tags[?(@.code=='catalog_inc')].list[*].code must be in ["start_time", "end_time", "mode"]
			
				> Note: **Condition TAGS_CATALOG_INC_VALID_ENUMS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='catalog_inc')].list[*].code must **not** be present in the payload
			
			- **condition TAGS_CATALOG_INC_START_TIME**: all elements of $.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='start_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}"]
			
				> Note: **Condition TAGS_CATALOG_INC_START_TIME** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='start_time')].value must **not** be present in the payload
			
			- **condition TAGS_CATALOG_INC_END_TIME**: all elements of $.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='end_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}"]
			
				> Note: **Condition TAGS_CATALOG_INC_END_TIME** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='end_time')].value must **not** be present in the payload
			
			- **condition TAGS_CATALOG_INC_MODE**: every element of $.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='mode')].value must be in ["start", "end"]
			
				> Note: **Condition TAGS_CATALOG_INC_MODE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='mode')].value must **not** be present in the payload
		
		- **TAGS_BAP_FEATURES** : All the following sub conditions must pass as per the api requirement
		
			- **condition TAGS_BAP_FEATURES_ITEM_1**: every element of $.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='1')].value must be in ["yes", "no"]
			
				> Note: **Condition TAGS_BAP_FEATURES_ITEM_1** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='1')].value must **not** be present in the payload
			
			- **condition TAGS_BAP_FEATURES_ITEM_2**: every element of $.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='2')].value must be in ["yes", "no"]
			
				> Note: **Condition TAGS_BAP_FEATURES_ITEM_2** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='2')].value must **not** be present in the payload
			
			- **condition TAGS_BAP_FEATURES_ITEM_3**: every element of $.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='3')].value must be in ["yes", "no"]
			
				> Note: **Condition TAGS_BAP_FEATURES_ITEM_3** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='3')].value must **not** be present in the payload
		
		- **TAGS_BAP_PROMOS** : All the following sub conditions must pass as per the api requirement
		
			- **condition TAGS_BAP_PROMOS_VALID_ENUMS**: every element of $.message.intent.tags[?(@.code=='bap_promos')].list[*].code must be in ["category", "from", "to"]
			
				> Note: **Condition TAGS_BAP_PROMOS_VALID_ENUMS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='bap_promos')].list[*].code must **not** be present in the payload
			
			- **condition TAGS_BAP_PROMOS_CATEGORY**: every element of $.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='category')].value must be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Bakery, Cakes & Dairy", "Pet Care", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks", "Gift Voucher"]
			
				> Note: **Condition TAGS_BAP_PROMOS_CATEGORY** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='category')].value must **not** be present in the payload
			
			- **condition TAGS_BAP_PROMOS_FROM**: all elements of $.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='from')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}"]
			
				> Note: **Condition TAGS_BAP_PROMOS_FROM** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='from')].value must **not** be present in the payload
			
			- **condition TAGS_BAP_PROMOS_TO**: all elements of $.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='to')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}"]
			
				> Note: **Condition TAGS_BAP_PROMOS_TO** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='to')].value must **not** be present in the payload
		
		- **TAGS_BNP_DEMAND_SIGNAL** : All the following sub conditions must pass as per the api requirement
		
			- **condition TAGS_BAP_PROMOS_VALID_ENUMS**: every element of $.message.intent.tags[?(@.code=='bnp_demand_signal')].list[*].code must be in ["search_term"]
			
				> Note: **Condition TAGS_BAP_PROMOS_VALID_ENUMS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='bnp_demand_signal')].list[*].code must **not** be present in the payload
			
			- **condition TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM**: $.message.intent.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='search_term')].value must be present in the payload
			
				> Note: **Condition TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.intent.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='search_term')].value must **not** be present in the payload

- **on_search** : All the following sub conditions must pass as per the api requirement

	- **ON_SEARCH_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_search"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_search"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_search"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["on_search"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_search"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_search"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **ON_SEARCH_CATALOG** : All the following sub conditions must pass as per the api requirement
	
		- **CATALOG_BPP_DESCRIPTOR** : All the following sub conditions must pass as per the api requirement
		
			- **condition BPP_DESCRIPTOR_NAME**: $.message.catalog['bpp/descriptor'].name must be present in the payload
			
			- **condition BPP_DESCRIPTOR_SYMBOL**: $.message.catalog['bpp/descriptor'].symbol must be present in the payload
			
			- **condition BPP_DESCRIPTOR_SHORT_DESC**: $.message.catalog['bpp/descriptor'].short_desc must be present in the payload
			
			- **condition BPP_DESCRIPTOR_LONG_DESC**: $.message.catalog['bpp/descriptor'].long_desc must be present in the payload
			
			- **condition BPP_DESCRIPTOR_IMAGES**: $.message.catalog['bpp/descriptor'].images[*] must be present in the payload
			
			- **BPP_DESCRIPTOR_TAGS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BPP_DESCRIPTORS_VALID_TAGS**: every element of $.message.catalog['bpp/descriptor'].tags[*].code must be in ["bpp_terms"]
				
					> Note: **Condition TAGS_BPP_DESCRIPTORS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.catalog['bpp/descriptor'].tags[*].code must **not** be present in the payload
				
				- **condition TAGS_BPP_DESCRIPTORS_VALID_ENUMS**: every element of $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[*].code must be in ["np_type", "accept_bap_terms", "collect_payment"]
				
					> Note: **Condition TAGS_BPP_DESCRIPTORS_VALID_ENUMS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[*].code must **not** be present in the payload
				
				- **BPP_DESCRIPTOR_TAGS_BPP_TERMS** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_BPP_TERMS_NP_TYPE**: every element of $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value must be in ["ISN", "MSN"]
					
					- **condition TAGS_BPP_TERMS_ACCEPT_BAP_TERMS**: every element of $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value must be in ["Y", "N"]
					
						> Note: **Condition TAGS_BPP_TERMS_ACCEPT_BAP_TERMS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value must **not** be present in the payload
					
					- **condition TAGS_BPP_TERMS_COLLECT_PAYMENT**: every element of $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='collect_payment')].value must be in ["Y", "N"]
					
						> Note: **Condition TAGS_BPP_TERMS_COLLECT_PAYMENT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='collect_payment')].value must **not** be present in the payload
					
					- **condition TAGS_BPP_TERMS_MANDATORY_ARBITRATION**: every element of $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value must be in ["true", "false"]
					
						> Note: **Condition TAGS_BPP_TERMS_MANDATORY_ARBITRATION** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value must **not** be present in the payload
		
		- **CATALOG_BPP_PROVIDERS** : All the following sub conditions must pass as per the api requirement
		
			- **condition PROVIDERS_ID**: $.message.catalog['bpp/providers'][*].id must be present in the payload
			
			- **condition PROVIDERS_RATING**: all elements of $.message.catalog['bpp/providers'][*].rating must follow every regex in ["^(?:[1-4](?:\\.\\d+)?|5(?:\\.0+)?|\\s*)$"]
			
				> Note: **Condition PROVIDERS_RATING** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.catalog['bpp/providers'][*].rating must **not** be present in the payload
			
			- **condition PROVIDERS_TIME_LABEL**: every element of $.message.catalog['bpp/providers'][*].time.label must be in ["enable", "disable"]
			
			- **condition PROVIDERS_TIME_TIMESTAMP**: all elements of $.message.catalog['bpp/providers'][*].time.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition PROVIDERS_TAGS_VALID_ENUMS**: every element of $.message.catalog['bpp/providers'][*].tags[*].code must be in ["timing", "close_timing", "serviceability", "order_value", "np_fees"]
			
			- **PROVIDERS_FULFILLMENTS** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_ID**: $.message.catalog['bpp/providers'][*].fulfillments[*].id must be present in the payload
				
				- **condition FULFILLMENTS_TYPE**: every element of $.message.catalog['bpp/providers'][*].fulfillments[*].type must be in ["Delivery", "Self-Pickup", "Buyer-Delivery"]
				
				- **condition FULFILLMENTS_CONTACT_PHONE**: all elements of $.message.catalog['bpp/providers'][*].fulfillments[*].contact.phone must follow every regex in ["^\\d{10,11}$"]
				
				- **condition FULFILLMENTS_CONTACT_EMAIL**: all elements of $.message.catalog['bpp/providers'][*].fulfillments[*].contact.email must follow every regex in ["^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"]
			
			- **PROVIDERS_DESCRIPTOR** : All the following sub conditions must pass as per the api requirement
			
				- **condition PROVIDERS_DESCRIPTOR_NAME**: $.message.catalog['bpp/providers'][*].descriptor.name must be present in the payload
				
				- **condition PROVIDERS_DESCRIPTOR_SYMBOL**: $.message.catalog['bpp/providers'][*].descriptor.symbol must be present in the payload
				
				- **condition PROVIDERS_DESCRIPTOR_SHORT_DESC**: $.message.catalog['bpp/providers'][*].descriptor.short_desc must be present in the payload
				
				- **condition PROVIDERS_DESCRIPTOR_LONG_DESC**: $.message.catalog['bpp/providers'][*].descriptor.long_desc must be present in the payload
				
				- **condition PROVIDERS_DESCRIPTOR_IMAGES**: $.message.catalog['bpp/providers'][*].descriptor.images[*] must be present in the payload
			
			- **condition PROVIDERS_TTL**: $.message.catalog['bpp/providers'][*].ttl must be present in the payload
			
			- **PROVIDERS_LOCATIONS** : All the following sub conditions must pass as per the api requirement
			
				- **condition LOCATIONS_ID**: $.message.catalog['bpp/providers'][*].locations[*].id must be present in the payload
				
				- **condition LOCATIONS_TIME_LABEL**: every element of $.message.catalog['bpp/providers'][*].locations[*].time.label must be in ["enable", "disable"]
				
				- **condition LOCATIONS_TIME_TIMESTAMP**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
				
				- **condition LOCATIONS_TIME_SCHEDULE**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.schedule.holidays[*] must follow every regex in ["^\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01])$"]
				
					> Note: **Condition LOCATIONS_TIME_SCHEDULE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.catalog['bpp/providers'][*].locations[*].time.schedule.holidays[*] must **not** be present in the payload
				
				- **condition LOCATIONS_TIME_SCHEDULE_TIMES**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*] must follow every regex in ["^(?:[01]\\d|2[0-3])[0-5]\\d$"]
				
					> Note: **Condition LOCATIONS_TIME_SCHEDULE_TIMES** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*] must **not** be present in the payload
				
				- **condition LOCATIONS_TIME_DAYS**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.days must follow every regex in ["^(?!.*\\b([1-7]),.*\\b\\1\\b)([1-7](,[1-7]){0,6})$"]
				
					> Note: **Condition LOCATIONS_TIME_DAYS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.catalog['bpp/providers'][*].locations[*].time.days must **not** be present in the payload
				
				- **condition LOCATIONS_TIME_FREQUENCY_RANGE**: any one of the following sub conditions must be met:
				
				  - **condition LOCATIONS_TIME_FREQUENCY_RANGE.1**: all of the following sub conditions must be met:
				
				    - **condition LOCATIONS_TIME_FREQUENCY_RANGE.1.1**: $.message.catalog['bpp/providers'][*].locations[*].time.frequency must be present in the payload
				    - **condition LOCATIONS_TIME_FREQUENCY_RANGE.1.2**: $.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*] must be present in the payload
				  - **condition LOCATIONS_TIME_FREQUENCY_RANGE.2**: $.message.catalog['bpp/providers'][*].locations[*].time.range.start must be present in the payload
				
				- **condition LOCATIONS_TIME_FREQUENCY**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.frequency must follow every regex in ["^P(?=\d|T)(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)W)?(?:(\d+)D)?(?:T(?=\d)(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?$"]
				
					> Note: **Condition LOCATIONS_TIME_FREQUENCY** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.catalog['bpp/providers'][*].locations[*].time.frequency must **not** be present in the payload
				
				- **condition LOCATIONS_GPS**: all elements of $.message.catalog['bpp/providers'][*].locations[*].gps must follow every regex in ["^\\d{2}\\.\\d{4,}\\s*,\\s*\\d{2}\\.\\d{4,}$"]
				
				- **condition RANGE_START_AND_END**: all of the following sub conditions must be met:
				
				  - **condition RANGE_START_AND_END.1**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.range.start must follow every regex in ["^([01]\\d|2[0-3])[0-5]\\d$"]
				  - **condition RANGE_START_AND_END.2**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.range.end must follow every regex in ["^([01]\\d|2[0-3])[0-5]\\d$"]
				
				- **condition LOCATIONS_ADDRESS_LOCALITY**: $.message.catalog['bpp/providers'][*].locations[*].address.locality must be present in the payload
				
				- **condition LOCATIONS_ADDRESS_STREET**: $.message.catalog['bpp/providers'][*].locations[*].address.street must be present in the payload
				
				- **condition LOCATIONS_ADDRESS_CITY**: $.message.catalog['bpp/providers'][*].locations[*].address.city must be present in the payload
				
				- **condition LOCATIONS_ADDRESS_AREA_CODE**: $.message.catalog['bpp/providers'][*].locations[*].address.area_code must be present in the payload
				
				- **condition LOCATIONS_ADDRESS_STATE**: $.message.catalog['bpp/providers'][*].locations[*].address.state must be present in the payload
				
				- **condition LOCATIONS_CIRCLE_RADIUS_UNIT**: every element of $.message.catalog['bpp/providers'][*].locations[*].circle.radius.unit must be in ["km"]
				
					> Note: **Condition LOCATIONS_CIRCLE_RADIUS_UNIT** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.catalog['bpp/providers'][*].locations[*].circle.radius.unit must **not** be present in the payload
			
			- **PROVIDERS_CATEGORIES** : All the following sub conditions must pass as per the api requirement
			
				- **condition CATEGORIES_ID**: all elements of $.message.catalog['bpp/providers'][*].categories[*].id must follow every regex in ["^[a-zA-Z0-9]{1,12}$"]
				
				- **condition CATEGORIES_DESCRIPTOR_NAME**: $.message.catalog['bpp/providers'][*].categories[*].descriptor.name must be present in the payload
				
				- **BPP_PROVIDER_CATEGORIES_TAGS** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[*].code must be in ["type", "attr", "np_fees"]
					
						> Note: **Condition TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[*].code must **not** be present in the payload
					
					- **TAGS_PROVIDER_CATEGORY_TYPE** : All the following sub conditions must pass as per the api requirement
					
						- **condition TAGS_PROVIDER_CATEGORY_TYPE_TYPE**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code must be in ["type", "attr"]
						
							> Note: **Condition TAGS_PROVIDER_CATEGORY_TYPE_TYPE** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code must **not** be present in the payload
						
						- **condition TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value must be in ["variant_group", "category"]
						
							> Note: **Condition TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value must **not** be present in the payload
						
						- **condition TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value must be in ["variant_group", "category"]
						
							> Note: **Condition TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value must **not** be present in the payload
					
					- **TAGS_PROVIDER_CATEGORY_NP_FEES** : All the following sub conditions must pass as per the api requirement
					
						- **condition TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code must be in ["channel_margin_type", "channel_margin_value"]
						
							> Note: **Condition TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code must **not** be present in the payload
						
						- **condition TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must be in ["percent", "amount"]
						
							> Note: **Condition TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must **not** be present in the payload
					
					- **TAGS_PROVIDER_CATEGORY_ATTR** : All the following sub conditions must pass as per the api requirement
					
						- **condition TAGS_PROVIDER_CATEGORY_TYPE_ATTR**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code must be in ["name", "seq"]
						
							> Note: **Condition TAGS_PROVIDER_CATEGORY_TYPE_ATTR** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code must **not** be present in the payload
			
			- **PROVIDERS_ITEMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition ITEMS_ID**: $.message.catalog['bpp/providers'][*].items[*].id must be present in the payload
				
				- **condition ITEMS_RATING**: all elements of $.message.catalog['bpp/providers'][*].items[*].rating must follow every regex in ["^(?:[1-4](?:\\.\\d+)?|5(?:\\.0+)?|\\s*)$"]
				
					> Note: **Condition ITEMS_RATING** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].rating must **not** be present in the payload
				
				- **condition ITEMS_TIME_LABEL**: every element of $.message.catalog['bpp/providers'][*].items[*].time.label must be in ["enable", "disable"]
				
				- **condition ITEMS_TIME_TIMESTAMP**: $.message.catalog['bpp/providers'][*].items[*].time.timestamp must be present in the payload
				
				- **condition ITEMS_DESCRIPTOR_NAME**: $.message.catalog['bpp/providers'][*].items[*].descriptor.name must be present in the payload
				
				- **condition ITEMS_DESCRIPTOR_SYMBOL**: $.message.catalog['bpp/providers'][*].items[*].descriptor.symbol must be present in the payload
				
				- **condition ITEMS_DESCRIPTOR_SHORT_DESC**: $.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc must be present in the payload
				
				- **condition ITEMS_DESCRIPTOR_CODE**: all elements of $.message.catalog['bpp/providers'][*].items[*].descriptor.code must follow every regex in ["^(1|5):"]
				
				- **condition ITEMS_DESCRIPTOR_IMAGES**: $.message.catalog['bpp/providers'][*].items[*].descriptor.images[*] must be present in the payload
				
				- **condition ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT**: every element of $.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.unit must be in ["unit", "dozen", "gram", "kilogram", "tonne", "litre", "millilitre"]
				
				- **condition ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE**: $.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.value must be present in the payload
				
				- **condition ITEMS_QUANTITY_AVAILABLE_COUNT**: every element of $.message.catalog['bpp/providers'][*].items[*].quantity.available.count must be in ["99", "0"]
				
				- **condition ITEMS_QUANTITY_MAXIMUM_COUNT**: $.message.catalog['bpp/providers'][*].items[*].quantity.maximum.count must be present in the payload
				
				- **condition ITEMS_PRICE_CURRENCY**: every element of $.message.catalog['bpp/providers'][*].items[*].price.currency must be in ["INR"]
				
				- **condition ITEMS_PRICE_VALUE**: $.message.catalog['bpp/providers'][*].items[*].price.value must be present in the payload
				
				- **condition ITEMS_PRICE_MAXIMUM_VALUE**: $.message.catalog['bpp/providers'][*].items[*].price.maximum_value must be present in the payload
				
				- **condition ITEMS_CATEGORY_ID**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Cleaning & Household", "Bakery, Cakes & Dairy", "Pet Care", "Stationery", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks", "Gift Voucher"]
				
				- **condition ITEMS_FULFILLMENT_ID**: $.message.catalog['bpp/providers'][*].items[*].fulfillment_id must be present in the payload
				
				- **condition ITEMS_LOCATION_ID**: $.message.catalog['bpp/providers'][*].items[*].location_id must be present in the payload
				
				- **condition ITEMS_RETURNABLE**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/returnable'] must be present in the payload
				
				- **condition ITEMS_CANCELLABLE**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/cancellable'] must be present in the payload
				
				- **condition ITEMS_SELLER_PICKUP_RETURN**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/seller_pickup_return'] must be present in the payload
				
				- **condition ITEMS_TIME_TO_SHIP**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/time_to_ship'] must be present in the payload
				
				- **condition ITEMS_AVAILABLE_ON_COD**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/available_on_cod'] must be present in the payload
				
				- **condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].additives_info must be present in the payload
				
					> Note: **Condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO** can be skipped if the following conditions are met:
					>
					> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Bakery, Cakes & Dairy", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Tinned and Processed Food", "Energy and Soft Drinks", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Snacks"]
				
				- **condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].brand_owner_FSSAI_license_no must be present in the payload
				
					> Note: **Condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO** can be skipped if the following conditions are met:
					>
					> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Bakery, Cakes & Dairy", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Tinned and Processed Food", "Energy and Soft Drinks", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Snacks"]
				
				- **condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].importer_FSSAI_license_no must be present in the payload
				
					> Note: **Condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO** can be skipped if the following conditions are met:
					>
					> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Bakery, Cakes & Dairy", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Tinned and Processed Food", "Energy and Soft Drinks", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Snacks"]
				
				- **condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].nutritional_info must be present in the payload
				
					> Note: **Condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO** can be skipped if the following conditions are met:
					>
					> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Bakery, Cakes & Dairy", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Tinned and Processed Food", "Energy and Soft Drinks", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Snacks"]
				
				- **condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].other_FSSAI_license_no must be present in the payload
				
					> Note: **Condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO** can be skipped if the following conditions are met:
					>
					> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Bakery, Cakes & Dairy", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Tinned and Processed Food", "Energy and Soft Drinks", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Snacks"]
				
				- **condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].common_or_generic_name_of_commodity must be present in the payload
				
					> Note: **Condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY** can be skipped if the following conditions are met:
					>
					> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Cleaning & Household", "Bakery, Cakes & Dairy", "Pet Care", "Stationery", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks"]
				
				- **condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_address must be present in the payload
				
					> Note: **Condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS** can be skipped if the following conditions are met:
					>
					> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Cleaning & Household", "Bakery, Cakes & Dairy", "Pet Care", "Stationery", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks"]
				
				- **condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_name must be present in the payload
				
					> Note: **Condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME** can be skipped if the following conditions are met:
					>
					> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Cleaning & Household", "Bakery, Cakes & Dairy", "Pet Care", "Stationery", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks"]
				
				- **condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].month_year_of_manufacture_packing_import must be present in the payload
				
					> Note: **Condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT** can be skipped if the following conditions are met:
					>
					> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Cleaning & Household", "Bakery, Cakes & Dairy", "Pet Care", "Stationery", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks"]
				
				- **ITEMS_TAGS** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_BPP_ITEMS_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].items[*].tags[*].code must be in ["origin", "veg_nonveg", "image", "timing", "np_fees"]
					
						> Note: **Condition TAGS_BPP_ITEMS_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[*].code must **not** be present in the payload
					
					- **condition TAGS_ITEMS_ORIGIN_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[*].code must be in ["country"]
					
						> Note: **Condition TAGS_ITEMS_ORIGIN_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[*].code must **not** be present in the payload
					
					- **condition ITEMS_TAGS_ORIGIN**: all elements of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[?(@.code=='country')].value must follow every regex in ["^[A-Z]{3}$"]
					
						> Note: **Condition ITEMS_TAGS_ORIGIN** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[?(@.code=='country')].value must **not** be present in the payload
					
					- **condition ITEMS_TAGS_TYPE**: every element of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='type')].value must be in ["back_image"]
					
						> Note: **Condition ITEMS_TAGS_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='type')].value must **not** be present in the payload
					
					- **condition ITEMS_TAGS_TYPE_VALID_URL**: all elements of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='url')].value must follow every regex in ["^(https?:\\/\\/)?(www\\.)?[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}(\/[^\\s]*)?$"]
					
						> Note: **Condition ITEMS_TAGS_TYPE_VALID_URL** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='url')].value must **not** be present in the payload
					
					- **TAGS_VEG_NONVEG** : All the following sub conditions must pass as per the api requirement
					
						- **condition TAGS_VEG_NONVEG_CODES**: every element of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code must be in ["veg", "non_veg", "egg"]
						
							> Note: **Condition TAGS_VEG_NONVEG_CODES** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code must **not** be present in the payload
						
						- **condition TAGS_VEG_NONVEG_VALUES**: every element of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value must be in ["yes"]
						
							> Note: **Condition TAGS_VEG_NONVEG_VALUES** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value must **not** be present in the payload
			
			- **PROVIDERS_OFFERS** : All the following sub conditions must pass as per the api requirement
			
				- **condition OFFERS_DESCRIPTOR_CODE**: every element of $.message.catalog['bpp/providers'][*].offers[*].descriptor.code must be in ["discount", "buyXgetY", "freebie", "slab", "combo", "delivery"]
				
					> Note: **Condition OFFERS_DESCRIPTOR_CODE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].descriptor.code must **not** be present in the payload
				
				- **BPP_PROVIDERS_OFFERS_TAGS** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_OFFERS_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[*].code must be in ["qualifier", "benefit", "meta", "finance_terms"]
					
						> Note: **Condition TAGS_OFFERS_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[*].code must **not** be present in the payload
					
					- **TAGS_QUALIFIER** : All the following sub conditions must pass as per the api requirement
					
						- **condition TAGS_QUALIFIER_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code must be in ["min_value", "item_count", "item_count_upper"]
						
							> Note: **Condition TAGS_QUALIFIER_VALID_TAGS** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code must **not** be present in the payload
					
					- **TAGS_BENEFIT** : All the following sub conditions must pass as per the api requirement
					
						- **condition TAGS_BENEFIT_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code must be in ["value_type", "value", "value_cap", "item_count", "item_id", "item_value"]
						
							> Note: **Condition TAGS_BENEFIT_VALID_TAGS** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code must **not** be present in the payload
						
						- **condition TAGS_BENEFIT_VALUE_TYPE**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value must be in ["percent", "amount"]
						
							> Note: **Condition TAGS_BENEFIT_VALUE_TYPE** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value must **not** be present in the payload
					
					- **TAGS_META** : All the following sub conditions must pass as per the api requirement
					
						- **condition TAGS_META_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code must be in ["additive", "auto"]
						
							> Note: **Condition TAGS_META_VALID_TAGS** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code must **not** be present in the payload
						
						- **condition TAGS_META_ADDITIVE**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value must be in ["yes", "no"]
						
							> Note: **Condition TAGS_META_ADDITIVE** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value must **not** be present in the payload
						
						- **condition TAGS_META_AUTO**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value must be in ["yes", "no"]
						
							> Note: **Condition TAGS_META_AUTO** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value must **not** be present in the payload
					
					- **TAGS_FINANCE_TERMS** : All the following sub conditions must pass as per the api requirement
					
						- **condition TAGS_FINANCE_TERMS_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code must be in ["subvention_type", "subvention_amount"]
						
							> Note: **Condition TAGS_FINANCE_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code must **not** be present in the payload
			
			- **PROVIDERS_TAGS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_PROVIDERS_VALID_TIMING_TAGS**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[?(@.code=='type')].value must be present in the payload
				
					> Note: **Condition TAGS_PROVIDERS_VALID_TIMING_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[?(@.code=='type')].value must **not** be present in the payload
				
				- **TAGS_PROVIDERS_SERVICEABILITY** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_PROVIDER_SERVICABILITY_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[*].code must be in ["location", "category", "type", "val", "day_from", "day_to", "time_from", "time_to", "unit"]
					
						> Note: **Condition TAGS_PROVIDER_SERVICABILITY_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[*].code must **not** be present in the payload
					
					- **condition TAGS_PROVIDERS_SERVICEABILITY_TYPE**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='type')].value must be in ["10", "11", "12", "13"]
					
					- **condition TAGS_PROVIDERS_SERVICEABILITY_UNIT**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='unit')].value must be in ["km", "geojson", "country", "pincode"]
				
				- **TAGS_PROVIDERS_ORDER_VALUE** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[*].code must be in ["min_value"]
					
						> Note: **Condition TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[*].code must **not** be present in the payload
					
					- **condition TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[?(@.code=='min_value')].value must be present in the payload
					
						> Note: **Condition TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[?(@.code=='min_value')].value must **not** be present in the payload
				
				- **TAGS_PROVIDERS_CATALOG_LINK** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_PROVIDERS_CATALOG_LINK_TYPE**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='catalog_link')].list[?(@.code=='type')].value must be in ["link", "inline"]
					
						> Note: **Condition TAGS_PROVIDERS_CATALOG_LINK_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='catalog_link')].list[?(@.code=='type')].value must **not** be present in the payload
				
				- **TAGS_PROVIDERS_TIMING** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_PROVIDER_TIMING_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[*].code must be in ["type", "location", "day_from", "day_to", "time_from", "time_to"]
					
						> Note: **Condition TAGS_PROVIDER_TIMING_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[*].code must **not** be present in the payload
				
				- **TAGS_PROVIDERS_NP_FEES** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_PROVIDER_NP_FEES_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[*].code must be in ["channel_margin_type", "channel_margin_value"]
					
						> Note: **Condition TAGS_PROVIDER_NP_FEES_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[*].code must **not** be present in the payload
					
					- **condition TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must be in ["percent", "amount"]
					
						> Note: **Condition TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must **not** be present in the payload
		
		- **CATALOG_BPP_FULFILLMENTS** : All the following sub conditions must pass as per the api requirement
		
			- **condition BPP_FULFILLMENTS_TYPE**: every element of $.message.catalog['bpp/fulfillments'][*].type must be in ["Delivery", "Self-Pickup", "Buyer-Delivery"]
			
				> Note: **Condition BPP_FULFILLMENTS_TYPE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.catalog['bpp/fulfillments'][*].type must **not** be present in the payload

- **select** : All the following sub conditions must pass as per the api requirement

	- **SELECT_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["select"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["select"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["select"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["select"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["select"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["select"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **SELECT_ORDER** : All the following sub conditions must pass as per the api requirement
	
		- **ORDER_PROVIDER** : All the following sub conditions must pass as per the api requirement
		
			- **condition ORDER_PROVIDER_ID**: $.message.order.provider.id must be present in the payload
			
			- **condition ORDER_PROVIDER_LOCATIONS_ID**: $.message.order.provider.locations[*].id must be present in the payload
		
		- **ORDER_ITEMS** : All the following sub conditions must pass as per the api requirement
		
			- **condition ITEMS_ID**: $.message.order.items[*].id must be present in the payload
			
			- **condition ITEMS_LOCATION_ID**: $.message.order.items[*].location_id must be present in the payload
			
				> Note: **Condition ITEMS_LOCATION_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.items[*].location_id must **not** be present in the payload
			
			- **condition ITEMS_QUANTITY_COUNT**: $.message.order.items[*].quantity.count must be present in the payload
		
		- **ORDER_OFFERS** : All the following sub conditions must pass as per the api requirement
		
			- **condition OFFERS_TAGS_SELECTION_APPLY**: every element of $.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value must be in ["yes", "no"]
			
				> Note: **Condition OFFERS_TAGS_SELECTION_APPLY** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value must **not** be present in the payload
		
		- **ORDER_FULFILLMENTS** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENT_END_LOCATION_GPS**: $.message.order.fulfillments[*].end.location.gps must be present in the payload
			
			- **condition FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE**: $.message.order.fulfillments[*].end.location.address.area_code must be present in the payload

- **on_select** : All the following sub conditions must pass as per the api requirement

	- **ON_SELECT_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_select"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_select"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_select"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["on_select"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_select"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_select"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **ON_SELECT_ORDER** : All the following sub conditions must pass as per the api requirement
	
		- **condition ORDER_PROVIDER**: $.message.order.provider.id must be present in the payload
		
		- **ORDER_ITEMS** : All the following sub conditions must pass as per the api requirement
		
			- **condition ITEMS_ID**: $.message.order.items[*].id must be present in the payload
			
			- **condition ITEMS_FULFILLMENT_ID**: any one of the following sub conditions must be met:
			
			  - **condition ITEMS_FULFILLMENT_ID.1**: $.message.order.items[*].fulfillment_ids[*] must be present in the payload
			  - **condition ITEMS_FULFILLMENT_ID.2**: $.message.order.items[*].fulfillment_id must be present in the payload
		
		- **ORDER_FULFILLMENTS** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENTS_ID**: $.message.order.fulfillments[*].id must be present in the payload
			
			- **condition FULFILLMENTS_TYPE**: $.message.order.fulfillments[*].type must be present in the payload
			
			- **condition FULFILLMENTS_PROVIDER_NAME**: $.message.order.fulfillments[*]['@ondc/org/provider_name'] must be present in the payload
			
			- **condition FULFILLMENTS_TRACKING**: $.message.order.fulfillments[*].tracking must be present in the payload
			
			- **condition FULFILLMENTS_CATEGORY**: $.message.order.fulfillments[*]['@ondc/org/category'] must be present in the payload
			
			- **condition FULFILLMENTS_TAT**: $.message.order.fulfillments[*]['@ondc/org/TAT'] must be present in the payload
			
			- **condition FULFILLMENTS_STATE_CODE**: every element of $.message.order.fulfillments[*].state.descriptor.code must be in ["Serviceable", "Non-serviceable"]
			
			- **FULFILLMENTS_TAGS_ORDER_DETAILS** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_TAGS_ORDER_VALID**: every element of $.message.order.fulfillments[*].tags[*].code must be in ["order_details"]
				
					> Note: **Condition FULFILLMENTS_TAGS_ORDER_VALID** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].tags[*].code must **not** be present in the payload
				
				- **condition FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code must be in ["weight_unit", "weight_value", "dim_unit", "length", "breadth", "height"]
				
					> Note: **Condition FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code must **not** be present in the payload
		
		- **ORDER_QUOTE** : All the following sub conditions must pass as per the api requirement
		
			- **condition QUOTE_PRICE_CURRENCY**: $.message.order.quote.price.currency must be present in the payload
			
			- **condition QUOTE_PRICE_VALUE**: $.message.order.quote.price.value must be present in the payload
			
			- **condition QUOTE_TTL**: $.message.order.quote.ttl must be present in the payload
			
			- **QUOTE_BREAKUP** : All the following sub conditions must pass as per the api requirement
			
				- **BREAKUP_ITEM** : All the following sub conditions must pass as per the api requirement
				
					- **condition BREAKUP_ITEM_ID**: $.message.order.quote.breakup[*]['@ondc/org/item_id'] must be present in the payload
					
					- **condition BREAKUP_ITEM_QUANTITY_COUNT**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must be present in the payload
					
						> Note: **Condition BREAKUP_ITEM_QUANTITY_COUNT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must **not** be present in the payload
					
					- **condition BREAKUP_ITEM_TITLE**: $.message.order.quote.breakup[*].title must be present in the payload
					
					- **condition BREAKUP_ITEM_TITLE_TYPE**: every element of $.message.order.quote.breakup[*]['@ondc/org/title_type'] must be in ["item", "delivery", "packing", "tax", "misc", "discount", "offer"]
					
					- **condition BREAKUP_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].price.currency must be present in the payload
					
					- **condition BREAKUP_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].price.value must be present in the payload
					
					- **BREAKUP_ITEM_ITEM** : All the following sub conditions must pass as per the api requirement
					
						- **condition BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT**: every element of $.message.order.quote.breakup[*].item.quantity.available.count must be in ["99", "0"]
						
							> Note: **Condition BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.quote.breakup[*].item.quantity.available.count must **not** be present in the payload
						
						- **condition BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT**: $.message.order.quote.breakup[*].item.quantity.maximum.count must be present in the payload
						
						- **condition BREAKUP_ITEM_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].item.price.currency must be present in the payload
						
						- **condition BREAKUP_ITEM_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].item.price.value must be present in the payload
						
						- **BREAKUP_ITEM_ITEM_TAGS** : All the following sub conditions must pass as per the api requirement
						
							- **condition BREAKUP_ITEM_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[*].code must be in ["quote", "np_fees", "offer"]
							
								> Note: **Condition BREAKUP_ITEM_VALID_TAGS** can be skipped if the following conditions are met:
								>
								> - **condition B**: $.message.order.quote.breakup[*].item.tags[*].code must **not** be present in the payload
							
							- **BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE** : All the following sub conditions must pass as per the api requirement
							
								- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must be in ["fulfillment", "order", "item"]
								
									> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE** can be skipped if the following conditions are met:
									>
									> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must **not** be present in the payload
								
								- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must be in ["delivery", "packaging", "misc"]
								
									> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE** can be skipped if the following conditions are met:
									>
									> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must **not** be present in the payload
		
		- **BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES** : All the following sub conditions must pass as per the api requirement
		
			- **condition BREAKUP_ITEM_ITEM_TAGS_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='np_fees')].list[*].code must be in ["id", "channel_margin_type", "channel_margin_value"]
			
				> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='np_fees')].list[*].code must **not** be present in the payload
			
			- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must be in ["percent", "amount"]
			
				> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must **not** be present in the payload
		
		- **BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER** : All the following sub conditions must pass as per the api requirement
		
			- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='offer')].list[*].code must be in ["id", "type", "auto", "additive", "item_id", "item_value", "item_count"]
			
				> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_VALID_TAGS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='offer')].list[*].code must **not** be present in the payload
			
			- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='type')].value must be in ["delivery", "discount"]
			
				> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='type')].value must **not** be present in the payload
			
			- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='auto')].value must be in ["yes", "no"]
			
				> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='auto')].value must **not** be present in the payload
			
			- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='additive')].value must be in ["yes", "no"]
			
				> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='additive')].value must **not** be present in the payload
		
		- **ERROR** : All the following sub conditions must pass as per the api requirement
		
			- **condition ERROR_TYPE**: $.error.type must be present in the payload
			
				> Note: **Condition ERROR_TYPE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.error.type must **not** be present in the payload
			
			- **condition ERROR_CODE**: $.error.code must be present in the payload
			
				> Note: **Condition ERROR_CODE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.error.code must **not** be present in the payload
			
			- **condition ERROR_MESSAGE**: $.error.message must be present in the payload
			
				> Note: **Condition ERROR_MESSAGE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.error.message must **not** be present in the payload

- **init** : All the following sub conditions must pass as per the api requirement

	- **INIT_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["init"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["init"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["init"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["init"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["init"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["init"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **INIT_ORDER** : All the following sub conditions must pass as per the api requirement
	
		- **ORDER_PROVIDER** : All the following sub conditions must pass as per the api requirement
		
			- **condition ORDER_PROVIDER_ID**: $.message.order.provider.id must be present in the payload
			
			- **condition ORDER_PROVIDER_LOCATIONS_ID**: $.message.order.provider.locations[*].id must be present in the payload
		
		- **ORDER_ITEMS** : All the following sub conditions must pass as per the api requirement
		
			- **condition ITEMS_ID**: $.message.order.items[*].id must be present in the payload
			
			- **condition ITEMS_FULFILLMENT_ID**: $.message.order.items[*].fulfillment_id must be present in the payload
			
			- **condition ITEMS_LOCATION_ID**: $.message.order.items[*].location_id must be present in the payload
			
				> Note: **Condition ITEMS_LOCATION_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.items[*].location_id must **not** be present in the payload
			
			- **condition ITEMS_QUANTITY_COUNT**: $.message.order.items[*].quantity.count must be present in the payload
			
			- **ITEMS_TAGS** : All the following sub conditions must pass as per the api requirement
			
				- **condition ITEMS_TAGS_VALID_TAGS**: every element of $.message.order.items[*].tags[*].code must be in ["np_fees"]
				
					> Note: **Condition ITEMS_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.items[*].tags[*].code must **not** be present in the payload
		
		- **ORDER_OFFERS** : All the following sub conditions must pass as per the api requirement
		
			- **condition OFFERS_ID**: $.message.order.offers[*].id must be present in the payload
			
				> Note: **Condition OFFERS_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.offers[*].id must **not** be present in the payload
			
			- **OFFERS_TAGS** : All the following sub conditions must pass as per the api requirement
			
				- **condition ITEMS_TAGS_SELECTION_VALID_TAGS**: every element of $.message.order.offers[*].tags[?(@.code=='selection')].list[*].code must be in ["apply"]
				
					> Note: **Condition ITEMS_TAGS_SELECTION_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.offers[*].tags[?(@.code=='selection')].list[*].code must **not** be present in the payload
				
				- **condition OFFERS_TAGS_SELECTION**: every element of $.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value must be in ["yes", "no"]
				
					> Note: **Condition OFFERS_TAGS_SELECTION** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value must **not** be present in the payload
		
		- **ORDER_BILLING** : All the following sub conditions must pass as per the api requirement
		
			- **BILLING_ADDRESS** : All the following sub conditions must pass as per the api requirement
			
				- **condition BILLING_ADDRESS_NAME**: $.message.order.billing.address.name must be present in the payload
				
				- **condition BILLING_ADDRESS_BUILDING**: $.message.order.billing.address.building must be present in the payload
				
				- **condition BILLING_ADDRESS_LOCALITY**: $.message.order.billing.address.locality must be present in the payload
				
				- **condition BILLING_ADDRESS_CITY**: $.message.order.billing.address.city must be present in the payload
				
				- **condition BILLING_ADDRESS_STATE**: $.message.order.billing.address.state must be present in the payload
				
				- **condition BILLING_ADDRESS_COUNTRY**: $.message.order.billing.address.country must be present in the payload
				
				- **condition BILLING_ADDRESS_AREA_CODE**: $.message.order.billing.address.area_code must be present in the payload
			
			- **condition BILLING_PHONE**: $.message.order.billing.phone must be present in the payload
			
			- **condition BILLING_NAME**: $.message.order.billing.name must be present in the payload
			
			- **condition BILLING_CREATED_AT**: $.message.order.billing.created_at must be present in the payload
			
			- **condition BILLING_UPDATED_AT**: $.message.order.billing.updated_at must be present in the payload
		
		- **ORDER_FULFILLMENTS** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENTS_ID**: $.message.order.fulfillments[*].id must be present in the payload
			
			- **condition FULFILLMENTS_TYPE**: $.message.order.fulfillments[*].type must be present in the payload
			
			- **condition FULFILLMENTS_END_LOCATION_GPS**: $.message.order.fulfillments[*].end.location.gps must be present in the payload
			
			- **FULFILLMENTS_END_LOCATION_ADDRESS** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_NAME**: $.message.order.fulfillments[*].end.location.address.name must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING**: $.message.order.fulfillments[*].end.location.address.building must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY**: $.message.order.fulfillments[*].end.location.address.locality must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_CITY**: $.message.order.fulfillments[*].end.location.address.city must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_STATE**: $.message.order.fulfillments[*].end.location.address.state must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY**: $.message.order.fulfillments[*].end.location.address.country must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE**: $.message.order.fulfillments[*].end.location.address.area_code must be present in the payload
			
			- **condition FULFILLMENTS_END_CONTACT_PHONE**: $.message.order.fulfillments[*].end.contact.phone must be present in the payload
		
		- **ORDER_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **ORDER_TAGS_BAP_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition ORDER_TAGS_VALID_TAGS**: every element of $.message.order.tags[*].code must be in ["bap_terms"]
				
					> Note: **Condition ORDER_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[*].code must **not** be present in the payload
				
				- **condition ORDER_TAGS_BAP_TERMS_VALID_TAGS**: every element of $.message.order.tags[?(@.code=='bap_terms')].list[*].code must be in ["finance_const_type", "finance_const_type"]
				
					> Note: **Condition ORDER_TAGS_BAP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[?(@.code=='bap_terms')].list[*].code must **not** be present in the payload
				
				- **condition ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE**: every element of $.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value must be in ["percent", "amount"]
				
					> Note: **Condition ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value must **not** be present in the payload

- **on_init** : All the following sub conditions must pass as per the api requirement

	- **ON_INIT_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_init"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_init"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_init"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["on_init"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_init"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_init"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **ON_INIT_ORDER** : All the following sub conditions must pass as per the api requirement
	
		- **ORDER_PROVIDER** : All the following sub conditions must pass as per the api requirement
		
			- **condition ORDER_PROVIDER_ID**: $.message.order.provider.id must be present in the payload
			
			- **condition ORDER_PROVIDER_LOCATIONS_ID**: $.message.order.provider.locations[*].id must be present in the payload
		
		- **ORDER_ITEMS** : All the following sub conditions must pass as per the api requirement
		
			- **condition ITEMS_ID**: $.message.order.items[*].id must be present in the payload
			
			- **condition ITEMS_FULFILLMENT_ID**: $.message.order.items[*].fulfillment_id must be present in the payload
			
			- **condition ITEMS_LOCATION_ID**: $.message.order.items[*].location_id must be present in the payload
			
				> Note: **Condition ITEMS_LOCATION_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.items[*].location_id must **not** be present in the payload
			
			- **condition ITEMS_QUANTITY_COUNT**: $.message.order.items[*].quantity.count must be present in the payload
			
			- **ITEMS_TAGS** : All the following sub conditions must pass as per the api requirement
			
				- **condition ITEMS_TAGS_VALID_TAGS**: every element of $.message.order.items[*].tags[*].code must be in ["np_fees"]
				
					> Note: **Condition ITEMS_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.items[*].tags[*].code must **not** be present in the payload
		
		- **ORDER_ITEMS_ADDITIONAL_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **condition ITEMS_TAGS_VALID_TAGS**: every element of $.message.order.items[*].tags[*].code must be in ["np_fees", "rto_action"]
			
				> Note: **Condition ITEMS_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.items[*].tags[*].code must **not** be present in the payload
			
			- **condition ITEMS_TAGS_NP_FEES_VALID_TAGS**: every element of $.message.order.items[*].tags[?(@.code=='np_fees')].list[*].code must be in ["id"]
			
				> Note: **Condition ITEMS_TAGS_NP_FEES_VALID_TAGS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.items[*].tags[?(@.code=='np_fees')].list[*].code must **not** be present in the payload
			
			- **condition ITEMS_TAGS_RTO_ACTION_VALID_TAGS**: every element of $.message.order.items[*].tags[?(@.code=='rto_action')].list[*].code must be in ["return_to_origin"]
			
				> Note: **Condition ITEMS_TAGS_RTO_ACTION_VALID_TAGS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.items[*].tags[?(@.code=='rto_action')].list[*].code must **not** be present in the payload
			
			- **condition ITEMS_TAGS_RTO_ACTION**: every element of $.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value must be in ["yes", "no"]
			
				> Note: **Condition ITEMS_TAGS_RTO_ACTION** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value must **not** be present in the payload
		
		- **ORDER_BILLING** : All the following sub conditions must pass as per the api requirement
		
			- **BILLING_ADDRESS** : All the following sub conditions must pass as per the api requirement
			
				- **condition BILLING_ADDRESS_NAME**: $.message.order.billing.address.name must be present in the payload
				
				- **condition BILLING_ADDRESS_BUILDING**: $.message.order.billing.address.building must be present in the payload
				
				- **condition BILLING_ADDRESS_LOCALITY**: $.message.order.billing.address.locality must be present in the payload
				
				- **condition BILLING_ADDRESS_CITY**: $.message.order.billing.address.city must be present in the payload
				
				- **condition BILLING_ADDRESS_STATE**: $.message.order.billing.address.state must be present in the payload
				
				- **condition BILLING_ADDRESS_COUNTRY**: $.message.order.billing.address.country must be present in the payload
				
				- **condition BILLING_ADDRESS_AREA_CODE**: $.message.order.billing.address.area_code must be present in the payload
			
			- **condition BILLING_PHONE**: $.message.order.billing.phone must be present in the payload
			
			- **condition BILLING_NAME**: $.message.order.billing.name must be present in the payload
			
			- **condition BILLING_CREATED_AT**: $.message.order.billing.created_at must be present in the payload
			
			- **condition BILLING_UPDATED_AT**: $.message.order.billing.updated_at must be present in the payload
		
		- **ORDER_FULFILLMENTS** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENTS_ID**: $.message.order.fulfillments[*].id must be present in the payload
			
			- **condition FULFILLMENTS_TYPE**: $.message.order.fulfillments[*].type must be present in the payload
			
			- **condition FULFILLMENTS_END_LOCATION_GPS**: $.message.order.fulfillments[*].end.location.gps must be present in the payload
			
			- **FULFILLMENTS_END_LOCATION_ADDRESS** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_NAME**: $.message.order.fulfillments[*].end.location.address.name must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING**: $.message.order.fulfillments[*].end.location.address.building must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY**: $.message.order.fulfillments[*].end.location.address.locality must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_CITY**: $.message.order.fulfillments[*].end.location.address.city must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_STATE**: $.message.order.fulfillments[*].end.location.address.state must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY**: $.message.order.fulfillments[*].end.location.address.country must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE**: $.message.order.fulfillments[*].end.location.address.area_code must be present in the payload
			
			- **condition FULFILLMENTS_END_CONTACT_PHONE**: $.message.order.fulfillments[*].end.contact.phone must be present in the payload
		
		- **ORDER_FULFILLMENTS_ADDITIONAL_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **FULFILLMENTS_TAGS_ORDER_DETAILS** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_TAGS_ORDER_VALID**: every element of $.message.order.fulfillments[*].tags[*].code must be in ["order_details"]
				
					> Note: **Condition FULFILLMENTS_TAGS_ORDER_VALID** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].tags[*].code must **not** be present in the payload
				
				- **condition FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code must be in ["weight_unit", "weight_value", "dim_unit", "length", "breadth", "height"]
				
					> Note: **Condition FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code must **not** be present in the payload
			
			- **condition FULFILLMENTS_TAGS_RTO_ACTION**: every element of $.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value must be in ["yes", "no"]
			
				> Note: **Condition FULFILLMENTS_TAGS_RTO_ACTION** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value must **not** be present in the payload
		
		- **ORDER_QUOTE** : All the following sub conditions must pass as per the api requirement
		
			- **condition QUOTE_PRICE_CURRENCY**: $.message.order.quote.price.currency must be present in the payload
			
			- **condition QUOTE_PRICE_VALUE**: $.message.order.quote.price.value must be present in the payload
			
			- **condition QUOTE_TTL**: $.message.order.quote.ttl must be present in the payload
			
			- **QUOTE_BREAKUP** : All the following sub conditions must pass as per the api requirement
			
				- **BREAKUP_ITEM** : All the following sub conditions must pass as per the api requirement
				
					- **condition BREAKUP_ITEM_ID**: $.message.order.quote.breakup[*]['@ondc/org/item_id'] must be present in the payload
					
					- **condition BREAKUP_ITEM_QUANTITY_COUNT**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must be present in the payload
					
						> Note: **Condition BREAKUP_ITEM_QUANTITY_COUNT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must **not** be present in the payload
					
					- **condition BREAKUP_ITEM_TITLE**: $.message.order.quote.breakup[*].title must be present in the payload
					
					- **condition BREAKUP_ITEM_TITLE_TYPE**: every element of $.message.order.quote.breakup[*]['@ondc/org/title_type'] must be in ["item", "delivery", "packing", "tax", "misc", "discount", "offer"]
					
					- **condition BREAKUP_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].price.currency must be present in the payload
					
					- **condition BREAKUP_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].price.value must be present in the payload
					
					- **BREAKUP_ITEM_ITEM** : All the following sub conditions must pass as per the api requirement
					
						- **condition BREAKUP_ITEM_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].item.price.currency must be present in the payload
						
						- **condition BREAKUP_ITEM_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].item.price.value must be present in the payload
						
						- **BREAKUP_ITEM_ITEM_TAGS** : All the following sub conditions must pass as per the api requirement
						
							- **condition BREAKUP_ITEM_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[*].code must be in ["quote", "np_fees", "offer"]
							
								> Note: **Condition BREAKUP_ITEM_VALID_TAGS** can be skipped if the following conditions are met:
								>
								> - **condition B**: $.message.order.quote.breakup[*].item.tags[*].code must **not** be present in the payload
							
							- **BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE** : All the following sub conditions must pass as per the api requirement
							
								- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must be in ["fulfillment", "order", "item"]
								
									> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE** can be skipped if the following conditions are met:
									>
									> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must **not** be present in the payload
								
								- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must be in ["delivery", "packaging", "misc"]
								
									> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE** can be skipped if the following conditions are met:
									>
									> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must **not** be present in the payload
		
		- **ORDER_QUOTE_ADDITIONAL_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **condition TAGS_ITEM_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[*].code must be in ["finance_terms", "np_fees", "quote"]
			
				> Note: **Condition TAGS_ITEM_VALID_TAGS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.quote.breakup[*].item.tags[*].code must **not** be present in the payload
			
			- **TAGS_FINANCE_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code must be in ["subvention_type", "subvention_amount", "provider_tax_number", "bank_account_no", "ifsc_code"]
				
					> Note: **Condition TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code must **not** be present in the payload
			
			- **BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_NP_FEES_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code must be in ["id", "channel_margin_type", "channel_margin_value"]
				
					> Note: **Condition TAGS_NP_FEES_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code must **not** be present in the payload
				
				- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must be in ["percent", "amount"]
				
					> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must **not** be present in the payload
		
		- **ORDER_PAYMENT** : All the following sub conditions must pass as per the api requirement
		
			- **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE**: every element of $.message.order.payment['@ondc/org/buyer_app_finder_fee_type'] must be in ["percent", "amount"]
			
			- **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT**: all of the following sub conditions must be met:
			
			  - **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT.1**: $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must be present in the payload
			  - **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT.2**: all elements of $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must follow every regex in ["^(\\d*.?\\d{1,2})$"]
			
			- **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE**: every element of $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must be in ["upi", "neft", "rtgs"]
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must **not** be present in the payload
		
		- **ORDER_PAYMENT_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **condition PAYMENT_TAGS_VALID_TAGS**: every element of $.message.order.payment.tags[*].code must be in ["bpp_terms", "bpp_collect"]
			
				> Note: **Condition PAYMENT_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.payment.tags[*].code must **not** be present in the payload
			
			- **TAGS_BPP_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BPP_TERMS_VALID_TAGS**: every element of $.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code must be in ["max_liability_cap", "max_liability", "mandatory_arbitration", "court_jurisdiction", "delay_interest", "np_type", "tax_number", "provider_tax_number", "accept_bap_terms"]
				
					> Note: **Condition TAGS_BPP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code must **not** be present in the payload
			
			- **TAGS_BPP_COLLECT** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BPP_COLLECT_VALID_TAGS**: every element of $.message.order.payment.tags[?(@.code=='bpp_collect')].list[*].code must be in ["success", "error"]
				
					> Note: **Condition TAGS_BPP_COLLECT_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment.tags[?(@.code=='bpp_collect')].list[*].code must **not** be present in the payload
				
				- **condition TAGS_BPP_COLLECT_SUCCESS**: every element of $.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value must be in ["Y", "N"]
				
					> Note: **Condition TAGS_BPP_COLLECT_SUCCESS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value must **not** be present in the payload
				
				- **condition TAGS_BPP_COLLECT_ERROR**: every element of $.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value must be in ["Y", "N"]
				
					> Note: **Condition TAGS_BPP_COLLECT_ERROR** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value must **not** be present in the payload
		
		- **ORDER_OFFERS** : All the following sub conditions must pass as per the api requirement
		
			- **condition OFFERS_DESCRIPTOR_CODE**: every element of $.message.order.offers[*].descriptor.code must be in ["discount", "buyXgetY", "freebie", "slab", "combo"]
			
				> Note: **Condition OFFERS_DESCRIPTOR_CODE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.offers[*].descriptor.code must **not** be present in the payload
		
		- **ORDER_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **TAGS_BAP_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BPP_TERMS_VALID_TAGS**: every element of $.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code must be in ["max_liability_cap", "max_liability", "mandatory_arbitration", "court_jurisdiction", "delay_interest", "np_type", "tax_number", "provider_tax_number", "accept_bap_terms"]
				
					> Note: **Condition TAGS_BPP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code must **not** be present in the payload

- **confirm** : All the following sub conditions must pass as per the api requirement

	- **CONFIRM_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["confirm"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["confirm"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["confirm"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["confirm"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["confirm"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["confirm"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **CONFIRM_ORDER** : All the following sub conditions must pass as per the api requirement
	
		- **condition ORDER_ID**: all of the following sub conditions must be met:
		
		  - **condition ORDER_ID.1**: $.message.order.id must be present in the payload
		  - **condition ORDER_ID.2**: all elements of $.message.order.id must follow every regex in ["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"]
		
		- **condition ORDER_STATE**: every element of $.message.order.state must be in ["Created", "Accepted", "Cancelled"]
		
		- **ORDER_PROVIDER** : All the following sub conditions must pass as per the api requirement
		
			- **condition ORDER_PROVIDER_ID**: $.message.order.provider.id must be present in the payload
			
			- **condition ORDER_PROVIDER_LOCATIONS_ID**: $.message.order.provider.locations[*].id must be present in the payload
		
		- **ORDER_ITEMS** : All the following sub conditions must pass as per the api requirement
		
			- **condition ITEMS_ID**: $.message.order.items[*].id must be present in the payload
			
			- **condition ITEMS_FULFILLMENT_ID**: $.message.order.items[*].fulfillment_id must be present in the payload
			
			- **condition ITEMS_LOCATION_ID**: $.message.order.items[*].location_id must be present in the payload
			
				> Note: **Condition ITEMS_LOCATION_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.items[*].location_id must **not** be present in the payload
			
			- **condition ITEMS_QUANTITY_COUNT**: $.message.order.items[*].quantity.count must be present in the payload
			
			- **ITEMS_TAGS** : All the following sub conditions must pass as per the api requirement
			
				- **condition ITEMS_TAGS_VALID_TAGS**: every element of $.message.order.items[*].tags[*].code must be in ["np_fees"]
				
					> Note: **Condition ITEMS_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.items[*].tags[*].code must **not** be present in the payload
		
		- **ORDER_BILLING** : All the following sub conditions must pass as per the api requirement
		
			- **BILLING_ADDRESS** : All the following sub conditions must pass as per the api requirement
			
				- **condition BILLING_ADDRESS_NAME**: $.message.order.billing.address.name must be present in the payload
				
				- **condition BILLING_ADDRESS_BUILDING**: $.message.order.billing.address.building must be present in the payload
				
				- **condition BILLING_ADDRESS_LOCALITY**: $.message.order.billing.address.locality must be present in the payload
				
				- **condition BILLING_ADDRESS_CITY**: $.message.order.billing.address.city must be present in the payload
				
				- **condition BILLING_ADDRESS_STATE**: $.message.order.billing.address.state must be present in the payload
				
				- **condition BILLING_ADDRESS_COUNTRY**: $.message.order.billing.address.country must be present in the payload
				
				- **condition BILLING_ADDRESS_AREA_CODE**: $.message.order.billing.address.area_code must be present in the payload
			
			- **condition BILLING_PHONE**: $.message.order.billing.phone must be present in the payload
			
			- **condition BILLING_NAME**: $.message.order.billing.name must be present in the payload
			
			- **condition BILLING_CREATED_AT**: $.message.order.billing.created_at must be present in the payload
			
			- **condition BILLING_UPDATED_AT**: $.message.order.billing.updated_at must be present in the payload
		
		- **ORDER_FULFILLMENTS** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENTS_ID**: $.message.order.fulfillments[*].id must be present in the payload
			
			- **condition FULFILLMENTS_TYPE**: $.message.order.fulfillments[*].type must be present in the payload
			
			- **condition FULFILLMENTS_END_LOCATION_GPS**: $.message.order.fulfillments[*].end.location.gps must be present in the payload
			
			- **FULFILLMENTS_END_LOCATION_ADDRESS** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_NAME**: $.message.order.fulfillments[*].end.location.address.name must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING**: $.message.order.fulfillments[*].end.location.address.building must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY**: $.message.order.fulfillments[*].end.location.address.locality must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_CITY**: $.message.order.fulfillments[*].end.location.address.city must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_STATE**: $.message.order.fulfillments[*].end.location.address.state must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY**: $.message.order.fulfillments[*].end.location.address.country must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE**: $.message.order.fulfillments[*].end.location.address.area_code must be present in the payload
			
			- **condition FULFILLMENTS_END_CONTACT_PHONE**: $.message.order.fulfillments[*].end.contact.phone must be present in the payload
		
		- **ORDER_FULFILLMENTS_ADDITIONAL_PROPERTIES** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENTS_END_PERSON_NAME**: $.message.order.fulfillments[*].end.person.name must be present in the payload
			
				> Note: **Condition FULFILLMENTS_END_PERSON_NAME** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.fulfillments[*].end.person.name must **not** be present in the payload
		
		- **ORDER_QUOTE** : All the following sub conditions must pass as per the api requirement
		
			- **condition QUOTE_PRICE_CURRENCY**: $.message.order.quote.price.currency must be present in the payload
			
			- **condition QUOTE_PRICE_VALUE**: $.message.order.quote.price.value must be present in the payload
			
			- **condition QUOTE_TTL**: $.message.order.quote.ttl must be present in the payload
			
			- **QUOTE_BREAKUP** : All the following sub conditions must pass as per the api requirement
			
				- **BREAKUP_ITEM** : All the following sub conditions must pass as per the api requirement
				
					- **condition BREAKUP_ITEM_ID**: $.message.order.quote.breakup[*]['@ondc/org/item_id'] must be present in the payload
					
					- **condition BREAKUP_ITEM_QUANTITY_COUNT**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must be present in the payload
					
						> Note: **Condition BREAKUP_ITEM_QUANTITY_COUNT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must **not** be present in the payload
					
					- **condition BREAKUP_ITEM_TITLE**: $.message.order.quote.breakup[*].title must be present in the payload
					
					- **condition BREAKUP_ITEM_TITLE_TYPE**: every element of $.message.order.quote.breakup[*]['@ondc/org/title_type'] must be in ["item", "delivery", "packing", "tax", "misc", "discount", "offer"]
					
					- **condition BREAKUP_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].price.currency must be present in the payload
					
					- **condition BREAKUP_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].price.value must be present in the payload
					
					- **BREAKUP_ITEM_ITEM** : All the following sub conditions must pass as per the api requirement
					
						- **condition BREAKUP_ITEM_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].item.price.currency must be present in the payload
						
						- **condition BREAKUP_ITEM_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].item.price.value must be present in the payload
						
						- **BREAKUP_ITEM_ITEM_TAGS** : All the following sub conditions must pass as per the api requirement
						
							- **condition BREAKUP_ITEM_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[*].code must be in ["quote", "np_fees", "offer"]
							
								> Note: **Condition BREAKUP_ITEM_VALID_TAGS** can be skipped if the following conditions are met:
								>
								> - **condition B**: $.message.order.quote.breakup[*].item.tags[*].code must **not** be present in the payload
							
							- **BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE** : All the following sub conditions must pass as per the api requirement
							
								- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must be in ["fulfillment", "order", "item"]
								
									> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE** can be skipped if the following conditions are met:
									>
									> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must **not** be present in the payload
								
								- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must be in ["delivery", "packaging", "misc"]
								
									> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE** can be skipped if the following conditions are met:
									>
									> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must **not** be present in the payload
		
		- **ORDER_QUOTE_ADDITIONAL_PROPERTIES** : All the following sub conditions must pass as per the api requirement
		
			- **condition QUOTE_TTL**: $.message.order.quote.ttl must be present in the payload
		
		- **ORDER_QUOTE_ADDITIONAL_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **TAGS_FINANCE_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code must be in ["subvention_type", "subvention_amount", "provider_tax_number", "bank_account_no", "ifsc_code"]
				
					> Note: **Condition TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code must **not** be present in the payload
			
			- **TAGS_FINANCE_TXN** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_FINANCE_TXN_LOAN_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_txn')].list[*].code must be in ["loan_completed", "down_payment", "loan_amount", "loan_provider", "transaction_id", "timestamp"]
				
					> Note: **Condition TAGS_FINANCE_TXN_LOAN_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_txn')].list[*].code must **not** be present in the payload
				
				- **condition TAGS_FINANCE_TXN_LOAN_COMPLETED**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_txn')].list[?(@.code=='loan_completed')].value must be in ["yes", "no"]
				
					> Note: **Condition TAGS_FINANCE_TXN_LOAN_COMPLETED** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_txn')].list[?(@.code=='loan_completed')].value must **not** be present in the payload
			
			- **BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_NP_FEES_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code must be in ["id", "channel_margin_type", "channel_margin_value"]
				
					> Note: **Condition TAGS_NP_FEES_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code must **not** be present in the payload
				
				- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must be in ["percent", "amount"]
				
					> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must **not** be present in the payload
		
		- **ORDER_PAYMENT** : All the following sub conditions must pass as per the api requirement
		
			- **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE**: every element of $.message.order.payment['@ondc/org/buyer_app_finder_fee_type'] must be in ["percent", "amount"]
			
			- **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT**: all of the following sub conditions must be met:
			
			  - **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT.1**: $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must be present in the payload
			  - **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT.2**: all elements of $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must follow every regex in ["^(\\d*.?\\d{1,2})$"]
			
			- **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE**: every element of $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must be in ["upi", "neft", "rtgs"]
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must **not** be present in the payload
		
		- **ORDER_PAYMENT_ADDITIONAL_PROPERTIES** : All the following sub conditions must pass as per the api requirement
		
			- **PAYMENT_PARAMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_CURRENCY**: $.message.order.payment.params.currency must be present in the payload
				
				- **condition PAYMENT_TRANSACTION_ID**: $.message.order.payment.params.transaction_id must be present in the payload
				
				- **condition PAYMENT_AMOUNT**: $.message.order.payment.params.amount must be present in the payload
			
			- **condition PAYMENT_STATUS**: $.message.order.payment.status must be present in the payload
			
			- **condition PAYMENT_TYPE**: $.message.order.payment.type must be present in the payload
			
			- **condition PAYMENT_COLLECTED_BY**: $.message.order.payment.collected_by must be present in the payload
		
		- **ORDER_PAYMENT_ADDITIONAL_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **TAGS_BPP_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BPP_TERMS_VALID_TAGS**: every element of $.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code must be in ["max_liability_cap", "max_liability", "mandatory_arbitration", "court_jurisdiction", "delay_interest", "np_type", "tax_number", "provider_tax_number", "accept_bap_terms"]
				
					> Note: **Condition TAGS_BPP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code must **not** be present in the payload
			
			- **TAGS_BAP_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BAP_TERMS_VALID_TAGS**: every element of $.message.order.payment.tags[?(@.code=='bap_terms')].list[*].code must be in ["static_terms", "tax_number"]
				
					> Note: **Condition TAGS_BAP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment.tags[?(@.code=='bap_terms')].list[*].code must **not** be present in the payload
		
		- **condition ORDER_CREATED_AT**: all of the following sub conditions must be met:
		
		  - **condition ORDER_CREATED_AT.1**: $.message.order.created_at must be present in the payload
		  - **condition ORDER_CREATED_AT.2**: all elements of $.message.order.created_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
		
		- **condition ORDER_UPDATED_AT**: all of the following sub conditions must be met:
		
		  - **condition ORDER_UPDATED_AT.1**: $.message.order.updated_at must be present in the payload
		  - **condition ORDER_UPDATED_AT.2**: all elements of $.message.order.updated_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
		
		- **ORDER_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **condition ORDER_TAGS_VALID_TAGS**: every element of $.message.order.tags[*].code must be in ["bap_terms", "bnp_receivables_claim", "bpp_terms"]
			
				> Note: **Condition ORDER_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.tags[*].code must **not** be present in the payload
			
			- **TAGS_BAP_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BAP_TERMS_VALID_TAGS**: every element of $.message.order.tags[?(@.code=='bap_terms')].list[*].code must be in ["finance_cost_type", "finance_cost_value", "tax_number"]
				
					> Note: **Condition TAGS_BAP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[?(@.code=='bap_terms')].list[*].code must **not** be present in the payload
				
				- **condition TAGS_BAP_TERMS_FINANCE_COST_TYPE**: every element of $.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_cost_type')].value must be in ["percent", "amount"]
				
					> Note: **Condition TAGS_BAP_TERMS_FINANCE_COST_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_cost_type')].value must **not** be present in the payload
			
			- **TAGS_BPP_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BPP_TERMS_VALID_TAGS**: every element of $.message.order.tags[?(@.code=='bpp_terms')].list[*].code must be in ["np_type", "tax_number", "provider_tax_number"]
				
					> Note: **Condition TAGS_BPP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[?(@.code=='bpp_terms')].list[*].code must **not** be present in the payload
				
				- **condition TAGS_BPP_TERMS_NP_TYPE**: every element of $.message.order.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value must be in ["MSN", "ISN"]
				
					> Note: **Condition TAGS_BPP_TERMS_NP_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value must **not** be present in the payload
			
			- **TAGS_BNP_RECEIVABLES_CLAIM** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BNP_RECEIVABLES_VALID_TAGS**: every element of $.message.order.tags[?(@.code=='bnp_receivables_claim')].list[*].code must be in ["type", "currency", "value"]
				
					> Note: **Condition TAGS_BNP_RECEIVABLES_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[?(@.code=='bnp_receivables_claim')].list[*].code must **not** be present in the payload

- **on_confirm** : All the following sub conditions must pass as per the api requirement

	- **ON_CONFIRM_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_confirm"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_confirm"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_confirm"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["on_confirm"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_confirm"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_confirm"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **ON_CONFIRM_ORDER** : All the following sub conditions must pass as per the api requirement
	
		- **condition ORDER_ID**: all of the following sub conditions must be met:
		
		  - **condition ORDER_ID.1**: $.message.order.id must be present in the payload
		  - **condition ORDER_ID.2**: all elements of $.message.order.id must follow every regex in ["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"]
		
		- **condition ORDER_STATE**: every element of $.message.order.state must be in ["Created", "Accepted", "Cancelled"]
		
		- **ORDER_PROVIDER** : All the following sub conditions must pass as per the api requirement
		
			- **condition ORDER_PROVIDER_ID**: $.message.order.provider.id must be present in the payload
			
			- **condition ORDER_PROVIDER_LOCATIONS_ID**: $.message.order.provider.locations[*].id must be present in the payload
		
		- **ORDER_ITEMS** : All the following sub conditions must pass as per the api requirement
		
			- **condition ITEMS_ID**: $.message.order.items[*].id must be present in the payload
			
			- **condition ITEMS_FULFILLMENT_ID**: $.message.order.items[*].fulfillment_id must be present in the payload
			
			- **condition ITEMS_LOCATION_ID**: $.message.order.items[*].location_id must be present in the payload
			
				> Note: **Condition ITEMS_LOCATION_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.items[*].location_id must **not** be present in the payload
			
			- **condition ITEMS_QUANTITY_COUNT**: $.message.order.items[*].quantity.count must be present in the payload
			
			- **ITEMS_TAGS** : All the following sub conditions must pass as per the api requirement
			
				- **condition ITEMS_TAGS_VALID_TAGS**: every element of $.message.order.items[*].tags[*].code must be in ["np_fees"]
				
					> Note: **Condition ITEMS_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.items[*].tags[*].code must **not** be present in the payload
		
		- **ORDER_BILLING** : All the following sub conditions must pass as per the api requirement
		
			- **BILLING_ADDRESS** : All the following sub conditions must pass as per the api requirement
			
				- **condition BILLING_ADDRESS_NAME**: $.message.order.billing.address.name must be present in the payload
				
				- **condition BILLING_ADDRESS_BUILDING**: $.message.order.billing.address.building must be present in the payload
				
				- **condition BILLING_ADDRESS_LOCALITY**: $.message.order.billing.address.locality must be present in the payload
				
				- **condition BILLING_ADDRESS_CITY**: $.message.order.billing.address.city must be present in the payload
				
				- **condition BILLING_ADDRESS_STATE**: $.message.order.billing.address.state must be present in the payload
				
				- **condition BILLING_ADDRESS_COUNTRY**: $.message.order.billing.address.country must be present in the payload
				
				- **condition BILLING_ADDRESS_AREA_CODE**: $.message.order.billing.address.area_code must be present in the payload
			
			- **condition BILLING_PHONE**: $.message.order.billing.phone must be present in the payload
			
			- **condition BILLING_NAME**: $.message.order.billing.name must be present in the payload
			
			- **condition BILLING_CREATED_AT**: $.message.order.billing.created_at must be present in the payload
			
			- **condition BILLING_UPDATED_AT**: $.message.order.billing.updated_at must be present in the payload
		
		- **ORDER_FULFILLMENTS** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENTS_ID**: $.message.order.fulfillments[*].id must be present in the payload
			
			- **condition FULFILLMENTS_TYPE**: $.message.order.fulfillments[*].type must be present in the payload
			
			- **condition FULFILLMENTS_END_LOCATION_GPS**: $.message.order.fulfillments[*].end.location.gps must be present in the payload
			
			- **FULFILLMENTS_END_LOCATION_ADDRESS** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_NAME**: $.message.order.fulfillments[*].end.location.address.name must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING**: $.message.order.fulfillments[*].end.location.address.building must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY**: $.message.order.fulfillments[*].end.location.address.locality must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_CITY**: $.message.order.fulfillments[*].end.location.address.city must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_STATE**: $.message.order.fulfillments[*].end.location.address.state must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY**: $.message.order.fulfillments[*].end.location.address.country must be present in the payload
				
				- **condition FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE**: $.message.order.fulfillments[*].end.location.address.area_code must be present in the payload
			
			- **condition FULFILLMENTS_END_CONTACT_PHONE**: $.message.order.fulfillments[*].end.contact.phone must be present in the payload
		
		- **ORDER_FULFILLMENTS_ADDITIONAL_PROPERTIES** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENTS_END_PERSON_NAME**: $.message.order.fulfillments[*].end.person.name must be present in the payload
			
				> Note: **Condition FULFILLMENTS_END_PERSON_NAME** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.fulfillments[*].end.person.name must **not** be present in the payload
		
		- **ORDER_QUOTE** : All the following sub conditions must pass as per the api requirement
		
			- **condition QUOTE_PRICE_CURRENCY**: $.message.order.quote.price.currency must be present in the payload
			
			- **condition QUOTE_PRICE_VALUE**: $.message.order.quote.price.value must be present in the payload
			
			- **condition QUOTE_TTL**: $.message.order.quote.ttl must be present in the payload
			
			- **QUOTE_BREAKUP** : All the following sub conditions must pass as per the api requirement
			
				- **BREAKUP_ITEM** : All the following sub conditions must pass as per the api requirement
				
					- **condition BREAKUP_ITEM_ID**: $.message.order.quote.breakup[*]['@ondc/org/item_id'] must be present in the payload
					
					- **condition BREAKUP_ITEM_QUANTITY_COUNT**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must be present in the payload
					
						> Note: **Condition BREAKUP_ITEM_QUANTITY_COUNT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must **not** be present in the payload
					
					- **condition BREAKUP_ITEM_TITLE**: $.message.order.quote.breakup[*].title must be present in the payload
					
					- **condition BREAKUP_ITEM_TITLE_TYPE**: every element of $.message.order.quote.breakup[*]['@ondc/org/title_type'] must be in ["item", "delivery", "packing", "tax", "misc", "discount", "offer"]
					
					- **condition BREAKUP_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].price.currency must be present in the payload
					
					- **condition BREAKUP_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].price.value must be present in the payload
					
					- **BREAKUP_ITEM_ITEM** : All the following sub conditions must pass as per the api requirement
					
						- **condition BREAKUP_ITEM_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].item.price.currency must be present in the payload
						
						- **condition BREAKUP_ITEM_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].item.price.value must be present in the payload
						
						- **BREAKUP_ITEM_ITEM_TAGS** : All the following sub conditions must pass as per the api requirement
						
							- **condition BREAKUP_ITEM_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[*].code must be in ["quote", "np_fees", "offer"]
							
								> Note: **Condition BREAKUP_ITEM_VALID_TAGS** can be skipped if the following conditions are met:
								>
								> - **condition B**: $.message.order.quote.breakup[*].item.tags[*].code must **not** be present in the payload
							
							- **BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE** : All the following sub conditions must pass as per the api requirement
							
								- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must be in ["fulfillment", "order", "item"]
								
									> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE** can be skipped if the following conditions are met:
									>
									> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must **not** be present in the payload
								
								- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must be in ["delivery", "packaging", "misc"]
								
									> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE** can be skipped if the following conditions are met:
									>
									> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must **not** be present in the payload
		
		- **ORDER_QUOTE_ADDITIONAL_PROPERTIES** : All the following sub conditions must pass as per the api requirement
		
			- **condition QUOTE_TTL**: $.message.order.quote.ttl must be present in the payload
		
		- **ORDER_QUOTE_ADDITIONAL_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **TAGS_FINANCE_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code must be in ["subvention_type", "subvention_amount", "provider_tax_number", "bank_account_no", "ifsc_code"]
				
					> Note: **Condition TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code must **not** be present in the payload
			
			- **TAGS_FINANCE_TXN** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_FINANCE_TXN_LOAN_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_txn')].list[*].code must be in ["loan_completed", "down_payment", "loan_amount", "loan_provider", "transaction_id", "timestamp"]
				
					> Note: **Condition TAGS_FINANCE_TXN_LOAN_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_txn')].list[*].code must **not** be present in the payload
				
				- **condition TAGS_FINANCE_TXN_LOAN_COMPLETED**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_txn')].list[?(@.code=='loan_completed')].value must be in ["yes", "no"]
				
					> Note: **Condition TAGS_FINANCE_TXN_LOAN_COMPLETED** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_txn')].list[?(@.code=='loan_completed')].value must **not** be present in the payload
			
			- **BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_NP_FEES_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code must be in ["id", "channel_margin_type", "channel_margin_value"]
				
					> Note: **Condition TAGS_NP_FEES_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code must **not** be present in the payload
				
				- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must be in ["percent", "amount"]
				
					> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must **not** be present in the payload
		
		- **ORDER_PAYMENT** : All the following sub conditions must pass as per the api requirement
		
			- **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE**: every element of $.message.order.payment['@ondc/org/buyer_app_finder_fee_type'] must be in ["percent", "amount"]
			
			- **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT**: all of the following sub conditions must be met:
			
			  - **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT.1**: $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must be present in the payload
			  - **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT.2**: all elements of $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must follow every regex in ["^(\\d*.?\\d{1,2})$"]
			
			- **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE**: every element of $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must be in ["upi", "neft", "rtgs"]
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must **not** be present in the payload
		
		- **ORDER_PAYMENT_ADDITIONAL_PROPERTIES** : All the following sub conditions must pass as per the api requirement
		
			- **PAYMENT_PARAMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_CURRENCY**: $.message.order.payment.params.currency must be present in the payload
				
				- **condition PAYMENT_TRANSACTION_ID**: $.message.order.payment.params.transaction_id must be present in the payload
				
				- **condition PAYMENT_AMOUNT**: $.message.order.payment.params.amount must be present in the payload
			
			- **condition PAYMENT_STATUS**: $.message.order.payment.status must be present in the payload
			
			- **condition PAYMENT_TYPE**: $.message.order.payment.type must be present in the payload
			
			- **condition PAYMENT_COLLECTED_BY**: $.message.order.payment.collected_by must be present in the payload
		
		- **ORDER_PAYMENT_ADDITIONAL_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **TAGS_BPP_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BPP_TERMS_VALID_TAGS**: every element of $.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code must be in ["max_liability_cap", "max_liability", "mandatory_arbitration", "court_jurisdiction", "delay_interest", "np_type", "tax_number", "provider_tax_number", "accept_bap_terms"]
				
					> Note: **Condition TAGS_BPP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code must **not** be present in the payload
			
			- **TAGS_BAP_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BAP_TERMS_VALID_TAGS**: every element of $.message.order.payment.tags[?(@.code=='bap_terms')].list[*].code must be in ["static_terms", "tax_number"]
				
					> Note: **Condition TAGS_BAP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment.tags[?(@.code=='bap_terms')].list[*].code must **not** be present in the payload
		
		- **condition ORDER_CREATED_AT**: all of the following sub conditions must be met:
		
		  - **condition ORDER_CREATED_AT.1**: $.message.order.created_at must be present in the payload
		  - **condition ORDER_CREATED_AT.2**: all elements of $.message.order.created_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
		
		- **condition ORDER_UPDATED_AT**: all of the following sub conditions must be met:
		
		  - **condition ORDER_UPDATED_AT.1**: $.message.order.updated_at must be present in the payload
		  - **condition ORDER_UPDATED_AT.2**: all elements of $.message.order.updated_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
		
		- **ORDER_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **condition ORDER_TAGS_VALID_TAGS**: every element of $.message.order.tags[*].code must be in ["bap_terms", "bnp_receivables_claim", "bpp_terms"]
			
				> Note: **Condition ORDER_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.tags[*].code must **not** be present in the payload
			
			- **TAGS_BAP_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BAP_TERMS_VALID_TAGS**: every element of $.message.order.tags[?(@.code=='bap_terms')].list[*].code must be in ["finance_cost_type", "finance_cost_value", "tax_number"]
				
					> Note: **Condition TAGS_BAP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[?(@.code=='bap_terms')].list[*].code must **not** be present in the payload
				
				- **condition TAGS_BAP_TERMS_FINANCE_COST_TYPE**: every element of $.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_cost_type')].value must be in ["percent", "amount"]
				
					> Note: **Condition TAGS_BAP_TERMS_FINANCE_COST_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_cost_type')].value must **not** be present in the payload
			
			- **TAGS_BPP_TERMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BPP_TERMS_VALID_TAGS**: every element of $.message.order.tags[?(@.code=='bpp_terms')].list[*].code must be in ["np_type", "tax_number", "provider_tax_number"]
				
					> Note: **Condition TAGS_BPP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[?(@.code=='bpp_terms')].list[*].code must **not** be present in the payload
				
				- **condition TAGS_BPP_TERMS_NP_TYPE**: every element of $.message.order.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value must be in ["MSN", "ISN"]
				
					> Note: **Condition TAGS_BPP_TERMS_NP_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value must **not** be present in the payload
			
			- **TAGS_BNP_RECEIVABLES_CLAIM** : All the following sub conditions must pass as per the api requirement
			
				- **condition TAGS_BNP_RECEIVABLES_VALID_TAGS**: every element of $.message.order.tags[?(@.code=='bnp_receivables_claim')].list[*].code must be in ["type", "currency", "value"]
				
					> Note: **Condition TAGS_BNP_RECEIVABLES_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[?(@.code=='bnp_receivables_claim')].list[*].code must **not** be present in the payload
	
	- **ON_CONFIRM_ORDER_ADDITIONAL_PROPERTIES** : All the following sub conditions must pass as per the api requirement
	
		- **ORDER_FULFILLMENTS_ADDITIONAL_PROPERTIES** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENTS_ONDC_ORG_PROVIDER_NAME**: $.message.order.fulfillments[*]['@ondc/org/provider_name'] must be present in the payload
			
			- **condition FULFILLMENTS_STATE_DESCRIPTOR_CODE**: $.message.order.fulfillments[*].state.descriptor.code must be present in the payload
			
			- **FULFILLMENTS_END_TIME** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_END_TIME_RANGE_START**: $.message.order.fulfillments[*].end.time.range.start must be present in the payload
				
					> Note: **Condition FULFILLMENTS_END_TIME_RANGE_START** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].end.time.range.start must **not** be present in the payload
				
				- **condition FULFILLMENTS_END_TIME_RANGE_END**: $.message.order.fulfillments[*].end.time.range.end must be present in the payload
				
					> Note: **Condition FULFILLMENTS_END_TIME_RANGE_END** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].end.time.range.end must **not** be present in the payload
			
			- **FULFILLMENTS_START** : All the following sub conditions must pass as per the api requirement
			
				- **FULFILLMENTS_START_LOCATION** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_LOCATION_ID**: $.message.order.fulfillments[*].start.location.id must be present in the payload
					
					- **condition FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME**: $.message.order.fulfillments[*].start.location.descriptor.name must be present in the payload
					
					- **condition FULFILLMENTS_START_LOCATION_GPS**: $.message.order.fulfillments[*].start.location.gps must be present in the payload
					
					- **FULFILLMENTS_START_LOCATION_ADDRESS** : All the following sub conditions must pass as per the api requirement
					
						- **condition FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY**: $.message.order.fulfillments[*].start.location.address.locality must be present in the payload
						
						- **condition FULFILLMENTS_START_LOCATION_ADDRESS_CITY**: $.message.order.fulfillments[*].start.location.address.city must be present in the payload
						
						- **condition FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE**: $.message.order.fulfillments[*].start.location.address.area_code must be present in the payload
						
						- **condition FULFILLMENTS_START_LOCATION_ADDRESS_STATE**: $.message.order.fulfillments[*].start.location.address.state must be present in the payload
				
				- **FULFILLMENTS_START_TIME** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_START_TIME_RANGE_START**: $.message.order.fulfillments[*].start.time.range.start must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_TIME_RANGE_START** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.time.range.start must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_TIME_RANGE_END**: $.message.order.fulfillments[*].start.time.range.end must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_TIME_RANGE_END** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.time.range.end must **not** be present in the payload
				
				- **FULFILLMENTS_START_INSTRUCTIONS** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_START_INSTRUCTIONS_CODE**: $.message.order.fulfillments[*].start.instructions.code must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_INSTRUCTIONS_CODE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.instructions.code must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_INSTRUCTIONS_NAME**: $.message.order.fulfillments[*].start.instructions.name must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_INSTRUCTIONS_NAME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.instructions.name must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC**: $.message.order.fulfillments[*].start.instructions.short_desc must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.instructions.short_desc must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC**: $.message.order.fulfillments[*].start.instructions.long_desc must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.instructions.long_desc must **not** be present in the payload
				
				- **FULFILLMENTS_START_CONTACT** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_START_CONTACT_PHONE**: $.message.order.fulfillments[*].start.contact.phone must be present in the payload
					
					- **condition FULFILLMENTS_START_CONTACT_EMAIL**: $.message.order.fulfillments[*].start.contact.email must be present in the payload

- **status** : All the following sub conditions must pass as per the api requirement

	- **STATUS_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["status"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["status"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["status"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["status"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["status"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["status"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **STATUS_ORDER** : All the following sub conditions must pass as per the api requirement
	
		- **condition ORDER_ID**: all of the following sub conditions must be met:
		
		  - **condition ORDER_ID.1**: $.message.order_id must be present in the payload
		  - **condition ORDER_ID.2**: all elements of $.message.order_id must follow every regex in ["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"]

- **on_status** : All the following sub conditions must pass as per the api requirement

	- **ON_STATUS_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_status"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_status"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_status"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["on_status"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_status"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_status"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **ON_STATUS_ORDER** : All the following sub conditions must pass as per the api requirement
	
		- **condition ORDER_ID**: all of the following sub conditions must be met:
		
		  - **condition ORDER_ID.1**: $.message.order.id must be present in the payload
		  - **condition ORDER_ID.2**: all elements of $.message.order.id must follow every regex in ["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"]
		
		- **condition ORDER_STATE**: every element of $.message.order.state must be in ["Created", "Accepted", "In-progress", "Completed", "Cancelled"]
		
		- **ORDER_PROVIDER** : All the following sub conditions must pass as per the api requirement
		
			- **condition ORDER_PROVIDER_ID**: $.message.order.provider.id must be present in the payload
			
			- **condition ORDER_PROVIDER_LOCATIONS_ID**: $.message.order.provider.locations[*].id must be present in the payload
		
		- **ORDER_CANCELLATION** : All the following sub conditions must pass as per the api requirement
		
			- **condition CANCELLATION_CANCELLED_BY**: $.message.order.cancellation.cancelled_by must be present in the payload
			
				> Note: **Condition CANCELLATION_CANCELLED_BY** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.cancellation.cancelled_by must **not** be present in the payload
			
			- **CANCELLATION_REASON** : All the following sub conditions must pass as per the api requirement
			
				- **condition CANCELLATION_REASON_ID**: $.message.order.cancellation.reason.id must be present in the payload
				
					> Note: **Condition CANCELLATION_REASON_ID** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.cancellation.reason.id must **not** be present in the payload
				
				- **condition CANCELLATION_REASON_STATE**: $.message.order.cancellation.reason.state must be present in the payload
				
					> Note: **Condition CANCELLATION_REASON_STATE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.cancellation.reason.state must **not** be present in the payload
		
		- **ORDER_ITEMS** : All the following sub conditions must pass as per the api requirement
		
			- **condition ITEMS_ID**: $.message.order.items[*].id must be present in the payload
			
			- **condition ITEMS_FULFILLMENT_ID**: $.message.order.items[*].fulfillment_id must be present in the payload
			
			- **condition ITEMS_LOCATION_ID**: $.message.order.items[*].location_id must be present in the payload
			
				> Note: **Condition ITEMS_LOCATION_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.items[*].location_id must **not** be present in the payload
			
			- **condition ITEMS_QUANTITY_COUNT**: $.message.order.items[*].quantity.count must be present in the payload
			
			- **ITEMS_TAGS** : All the following sub conditions must pass as per the api requirement
			
				- **condition ITEMS_TAGS_VALID_TAGS**: every element of $.message.order.items[*].tags[*].code must be in ["np_fees"]
				
					> Note: **Condition ITEMS_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.items[*].tags[*].code must **not** be present in the payload
		
		- **ORDER_BILLING** : All the following sub conditions must pass as per the api requirement
		
			- **BILLING_ADDRESS** : All the following sub conditions must pass as per the api requirement
			
				- **condition BILLING_ADDRESS_NAME**: $.message.order.billing.address.name must be present in the payload
				
				- **condition BILLING_ADDRESS_BUILDING**: $.message.order.billing.address.building must be present in the payload
				
				- **condition BILLING_ADDRESS_LOCALITY**: $.message.order.billing.address.locality must be present in the payload
				
				- **condition BILLING_ADDRESS_CITY**: $.message.order.billing.address.city must be present in the payload
				
				- **condition BILLING_ADDRESS_STATE**: $.message.order.billing.address.state must be present in the payload
				
				- **condition BILLING_ADDRESS_COUNTRY**: $.message.order.billing.address.country must be present in the payload
				
				- **condition BILLING_ADDRESS_AREA_CODE**: $.message.order.billing.address.area_code must be present in the payload
			
			- **condition BILLING_PHONE**: $.message.order.billing.phone must be present in the payload
			
			- **condition BILLING_NAME**: $.message.order.billing.name must be present in the payload
			
			- **condition BILLING_CREATED_AT**: $.message.order.billing.created_at must be present in the payload
			
			- **condition BILLING_UPDATED_AT**: $.message.order.billing.updated_at must be present in the payload
		
		- **ORDER_FULFILLMENTS** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENTS_ID**: $.message.order.fulfillments[*].id must be present in the payload
			
			- **condition FULFILLMENTS_STATE_DESCRIPTOR_CODE**: all of the following sub conditions must be met:
			
			  - **condition FULFILLMENTS_STATE_DESCRIPTOR_CODE.1**: $.message.order.fulfillments[*].state.descriptor.code must be present in the payload
			  - **condition FULFILLMENTS_STATE_DESCRIPTOR_CODE.2**: every element of $.message.order.fulfillments[*].state.descriptor.code must be in ["Pending", "Packed", "Agent-assigned", "Order-picked-up", "Out-for-delivery", "Order-delivered", "Cancelled", "RTO-Initiated", "RTO-Disposed", "RTO-Delivered"]
			
			- **condition FULFILLMENTS_TYPE**: $.message.order.fulfillments[*].type must be present in the payload
			
			- **condition FULFILLMENTS_ONDC_ORG_PROVIDER_NAME**: $.message.order.fulfillments[*]['@ondc/org/provider_name'] must be present in the payload
			
			- **condition FULFILLMENTS_TRACKING**: $.message.order.fulfillments[*].tracking must be present in the payload
			
			- **condition FULFILLMENTS_ONDC_ORG_TAT**: $.message.order.fulfillments[*]['@ondc/org/TAT'] must be present in the payload
			
			- **FULFILLMENTS_START** : All the following sub conditions must pass as per the api requirement
			
				- **FULFILLMENTS_START_LOCATION** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME**: $.message.order.fulfillments[*].start.location.descriptor.name must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.location.descriptor.name must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_LOCATION_GPS**: $.message.order.fulfillments[*].start.location.gps must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_LOCATION_GPS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.location.gps must **not** be present in the payload
					
					- **FULFILLMENTS_START_LOCATION_ADDRESS** : All the following sub conditions must pass as per the api requirement
					
						- **condition FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY**: $.message.order.fulfillments[*].start.location.address.locality must be present in the payload
						
							> Note: **Condition FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.fulfillments[*].start.location.address.locality must **not** be present in the payload
						
						- **condition FULFILLMENTS_START_LOCATION_ADDRESS_CITY**: $.message.order.fulfillments[*].start.location.address.city must be present in the payload
						
							> Note: **Condition FULFILLMENTS_START_LOCATION_ADDRESS_CITY** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.fulfillments[*].start.location.address.city must **not** be present in the payload
						
						- **condition FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE**: $.message.order.fulfillments[*].start.location.address.area_code must be present in the payload
						
							> Note: **Condition FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.fulfillments[*].start.location.address.area_code must **not** be present in the payload
						
						- **condition FULFILLMENTS_START_LOCATION_ADDRESS_STATE**: $.message.order.fulfillments[*].start.location.address.state must be present in the payload
						
							> Note: **Condition FULFILLMENTS_START_LOCATION_ADDRESS_STATE** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.fulfillments[*].start.location.address.state must **not** be present in the payload
				
				- **FULFILLMENTS_START_TIME** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_START_TIME_RANGE_START**: $.message.order.fulfillments[*].start.time.range.start must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_TIME_RANGE_START** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.time.range.start must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_TIME_RANGE_END**: $.message.order.fulfillments[*].start.time.range.end must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_TIME_RANGE_END** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.time.range.end must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_TIME_TIMESTAMP**: $.message.order.fulfillments[*].start.time.timestamp must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_TIME_TIMESTAMP** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.time.timestamp must **not** be present in the payload
				
				- **FULFILLMENTS_START_INSTRUCTIONS** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_START_INSTRUCTIONS_CODE**: all of the following sub conditions must be met:
					
					  - **condition FULFILLMENTS_START_INSTRUCTIONS_CODE.1**: $.message.order.fulfillments[*].start.instructions.code must be present in the payload
					  - **condition FULFILLMENTS_START_INSTRUCTIONS_CODE.2**: every element of $.message.order.fulfillments[*].start.instructions.code must be in ["1", "2", "3", "4"]
					
						> Note: **Condition FULFILLMENTS_START_INSTRUCTIONS_CODE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.instructions.code must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_INSTRUCTIONS_NAME**: $.message.order.fulfillments[*].start.instructions.name must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_INSTRUCTIONS_NAME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.instructions.name must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC**: $.message.order.fulfillments[*].start.instructions.short_desc must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.instructions.short_desc must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC**: $.message.order.fulfillments[*].start.instructions.long_desc must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.instructions.long_desc must **not** be present in the payload
				
				- **FULFILLMENTS_START_CONTACT** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_START_CONTACT_PHONE**: $.message.order.fulfillments[*].start.contact.phone must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_CONTACT_PHONE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.contact.phone must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_CONTACT_EMAIL**: $.message.order.fulfillments[*].start.contact.email must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_CONTACT_EMAIL** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.contact.email must **not** be present in the payload
			
			- **FULFILLMENTS_END** : All the following sub conditions must pass as per the api requirement
			
				- **FULFILLMENTS_END_LOCATION** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_END_LOCATION_GPS**: $.message.order.fulfillments[*].end.location.gps must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_LOCATION_GPS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.location.gps must **not** be present in the payload
					
					- **FULFILLMENTS_END_LOCATION_ADDRESS** : All the following sub conditions must pass as per the api requirement
					
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_NAME**: $.message.order.fulfillments[*].end.location.address.name must be present in the payload
						
							> Note: **Condition FULFILLMENTS_END_LOCATION_ADDRESS_NAME** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.fulfillments[*].end.location.address.name must **not** be present in the payload
						
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING**: $.message.order.fulfillments[*].end.location.address.building must be present in the payload
						
							> Note: **Condition FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.fulfillments[*].end.location.address.building must **not** be present in the payload
						
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY**: $.message.order.fulfillments[*].end.location.address.locality must be present in the payload
						
							> Note: **Condition FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.fulfillments[*].end.location.address.locality must **not** be present in the payload
						
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY**: $.message.order.fulfillments[*].end.location.address.country must be present in the payload
						
							> Note: **Condition FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.fulfillments[*].end.location.address.country must **not** be present in the payload
						
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_CITY**: $.message.order.fulfillments[*].end.location.address.city must be present in the payload
						
							> Note: **Condition FULFILLMENTS_END_LOCATION_ADDRESS_CITY** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.fulfillments[*].end.location.address.city must **not** be present in the payload
						
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE**: $.message.order.fulfillments[*].end.location.address.area_code must be present in the payload
						
							> Note: **Condition FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.fulfillments[*].end.location.address.area_code must **not** be present in the payload
						
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_STATE**: $.message.order.fulfillments[*].end.location.address.state must be present in the payload
						
							> Note: **Condition FULFILLMENTS_END_LOCATION_ADDRESS_STATE** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.fulfillments[*].end.location.address.state must **not** be present in the payload
				
				- **FULFILLMENTS_END_TIME** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_END_TIME_RANGE_START**: $.message.order.fulfillments[*].end.time.range.start must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_TIME_RANGE_START** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.time.range.start must **not** be present in the payload
					
					- **condition FULFILLMENTS_END_TIME_RANGE_END**: $.message.order.fulfillments[*].end.time.range.end must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_TIME_RANGE_END** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.time.range.end must **not** be present in the payload
					
					- **condition FULFILLMENTS_END_TIME_TIMESTAMP**: $.message.order.fulfillments[*].end.time.timestamp must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_TIME_TIMESTAMP** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.time.timestamp must **not** be present in the payload
				
				- **FULFILLMENTS_END_INSTRUCTIONS** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_END_INSTRUCTIONS_CODE**: $.message.order.fulfillments[*].end.instructions.code must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_INSTRUCTIONS_CODE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.instructions.code must **not** be present in the payload
					
					- **condition FULFILLMENTS_END_INSTRUCTIONS_NAME**: $.message.order.fulfillments[*].end.instructions.name must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_INSTRUCTIONS_NAME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.instructions.name must **not** be present in the payload
					
					- **condition FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC**: $.message.order.fulfillments[*].end.instructions.short_desc must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.instructions.short_desc must **not** be present in the payload
					
					- **condition FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC**: $.message.order.fulfillments[*].end.instructions.long_desc must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.instructions.long_desc must **not** be present in the payload
				
				- **FULFILLMENTS_END_CONTACT** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_END_CONTACT_PHONE**: $.message.order.fulfillments[*].end.contact.phone must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_CONTACT_PHONE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.contact.phone must **not** be present in the payload
					
					- **condition FULFILLMENTS_END_CONTACT_EMAIL**: $.message.order.fulfillments[*].end.contact.email must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_CONTACT_EMAIL** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.contact.email must **not** be present in the payload
			
			- **FULFILLMENTS_AGENT** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_AGENT_PHONE**: $.message.order.fulfillments[*].agent.phone must be present in the payload
				
					> Note: **Condition FULFILLMENTS_AGENT_PHONE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].agent.phone must **not** be present in the payload
			
			- **FULFILLMENTS_VEHICLE** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_VEHICLE_REGISTRATION**: $.message.order.fulfillments[*].vehicle.registration must be present in the payload
				
					> Note: **Condition FULFILLMENTS_VEHICLE_REGISTRATION** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].vehicle.registration must **not** be present in the payload
			
			- **FULFILLMENTS_TAGS** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_TAGS_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[*].code must be in ["state", "routing", "tracking", "fulfillment_delay", "order_details"]
				
					> Note: **Condition FULFILLMENTS_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].tags[*].code must **not** be present in the payload
				
				- **TAGS_STATE** : All the following sub conditions must pass as per the api requirement
				
					- **condition STATE_READY_TO_SHIP_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='state')].list[*].code must be in ["ready_to_ship"]
					
						> Note: **Condition STATE_READY_TO_SHIP_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='state')].list[*].code must **not** be present in the payload
					
					- **condition STATE_READY_TO_SHIP**: $.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value must be present in the payload
					
						> Note: **Condition STATE_READY_TO_SHIP** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value must **not** be present in the payload
				
				- **TAGS_ROUTING** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_ROUTING_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='routing')].list[*].code must be in ["type"]
					
						> Note: **Condition TAGS_ROUTING_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='routing')].list[*].code must **not** be present in the payload
					
					- **condition ROUTING_TYPE**: $.message.order.fulfillments[*].tags[?(@.code=='routing')].list[?(@.code=='type')].value must be present in the payload
					
						> Note: **Condition ROUTING_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='routing')].list[?(@.code=='type')].value must **not** be present in the payload
				
				- **TAGS_TRACKING** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_TRACKING_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[*].code must be in ["gps_enabled", "url_enabled", "url"]
					
						> Note: **Condition TAGS_TRACKING_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[*].code must **not** be present in the payload
					
					- **condition TRACKING_GPS_ENABLED**: $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='gps_enabled')].value must be present in the payload
					
						> Note: **Condition TRACKING_GPS_ENABLED** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='gps_enabled')].value must **not** be present in the payload
					
					- **condition TRACKING_URL_ENABLED**: $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url_enabled')].value must be present in the payload
					
						> Note: **Condition TRACKING_URL_ENABLED** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url_enabled')].value must **not** be present in the payload
					
					- **condition TRACKING_URL**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url')].value must follow every regex in ["^https?://.*$"]
					
						> Note: **Condition TRACKING_URL** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url')].value must **not** be present in the payload
				
				- **TAGS_FULFILLMENT_DELAY** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_FULFILLMENT_DELAY_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[*].code must be in ["state", "reason_id", "timestamp"]
					
						> Note: **Condition TAGS_FULFILLMENT_DELAY_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[*].code must **not** be present in the payload
					
					- **condition DELAY_STATE**: every element of $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='state')].value must be in ["Order-picked-up", "Order-delivered"]
					
						> Note: **Condition DELAY_STATE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='state')].value must **not** be present in the payload
					
					- **condition DELAY_REASON_ID**: $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='reason_id')].value must be present in the payload
					
						> Note: **Condition DELAY_REASON_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='reason_id')].value must **not** be present in the payload
					
					- **condition DELAY_TIMESTAMP**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='timestamp')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition DELAY_TIMESTAMP** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='timestamp')].value must **not** be present in the payload
				
				- **TAGS_ORDER_DETAILS** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_ORDER_DETAILS_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code must be in ["id", "weight_unit", "weight_value", "dim_unit", "length", "breadth", "height"]
					
						> Note: **Condition TAGS_ORDER_DETAILS_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code must **not** be present in the payload
					
					- **condition ORDER_ID**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='id')].value must be present in the payload
					
						> Note: **Condition ORDER_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='id')].value must **not** be present in the payload
					
					- **condition ORDER_WEIGHT_UNIT**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value must be present in the payload
					
						> Note: **Condition ORDER_WEIGHT_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value must **not** be present in the payload
					
					- **condition ORDER_WEIGHT_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value must be present in the payload
					
						> Note: **Condition ORDER_WEIGHT_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value must **not** be present in the payload
					
					- **condition ORDER_DIM_UNIT**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value must be present in the payload
					
						> Note: **Condition ORDER_DIM_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value must **not** be present in the payload
					
					- **condition ORDER_LENGTH**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value must be present in the payload
					
						> Note: **Condition ORDER_LENGTH** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value must **not** be present in the payload
					
					- **condition ORDER_BREADTH**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value must be present in the payload
					
						> Note: **Condition ORDER_BREADTH** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value must **not** be present in the payload
					
					- **condition ORDER_HEIGHT**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value must be present in the payload
					
						> Note: **Condition ORDER_HEIGHT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value must **not** be present in the payload
		
		- **ORDER_QUOTE** : All the following sub conditions must pass as per the api requirement
		
			- **condition QUOTE_PRICE_CURRENCY**: $.message.order.quote.price.currency must be present in the payload
			
			- **condition QUOTE_PRICE_VALUE**: $.message.order.quote.price.value must be present in the payload
			
			- **condition QUOTE_TTL**: $.message.order.quote.ttl must be present in the payload
			
			- **QUOTE_BREAKUP** : All the following sub conditions must pass as per the api requirement
			
				- **BREAKUP_ITEM** : All the following sub conditions must pass as per the api requirement
				
					- **condition BREAKUP_ITEM_ID**: $.message.order.quote.breakup[*]['@ondc/org/item_id'] must be present in the payload
					
					- **condition BREAKUP_ITEM_QUANTITY_COUNT**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must be present in the payload
					
						> Note: **Condition BREAKUP_ITEM_QUANTITY_COUNT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must **not** be present in the payload
					
					- **condition BREAKUP_ITEM_TITLE**: $.message.order.quote.breakup[*].title must be present in the payload
					
					- **condition BREAKUP_ITEM_TITLE_TYPE**: every element of $.message.order.quote.breakup[*]['@ondc/org/title_type'] must be in ["item", "delivery", "packing", "tax", "misc", "discount", "offer"]
					
					- **condition BREAKUP_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].price.currency must be present in the payload
					
					- **condition BREAKUP_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].price.value must be present in the payload
					
					- **BREAKUP_ITEM_ITEM** : All the following sub conditions must pass as per the api requirement
					
						- **condition BREAKUP_ITEM_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].item.price.currency must be present in the payload
						
						- **condition BREAKUP_ITEM_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].item.price.value must be present in the payload
						
						- **BREAKUP_ITEM_ITEM_TAGS** : All the following sub conditions must pass as per the api requirement
						
							- **condition BREAKUP_ITEM_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[*].code must be in ["quote", "np_fees", "offer"]
							
								> Note: **Condition BREAKUP_ITEM_VALID_TAGS** can be skipped if the following conditions are met:
								>
								> - **condition B**: $.message.order.quote.breakup[*].item.tags[*].code must **not** be present in the payload
							
							- **BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE** : All the following sub conditions must pass as per the api requirement
							
								- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must be in ["fulfillment", "order", "item"]
								
									> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE** can be skipped if the following conditions are met:
									>
									> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must **not** be present in the payload
								
								- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must be in ["delivery", "packaging", "misc"]
								
									> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE** can be skipped if the following conditions are met:
									>
									> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must **not** be present in the payload
		
		- **ORDER_QUOTE_ADDITIONAL_PROPERTIES** : All the following sub conditions must pass as per the api requirement
		
			- **condition QUOTE_TTL**: $.message.order.quote.ttl must be present in the payload
		
		- **ORDER_PAYMENT** : All the following sub conditions must pass as per the api requirement
		
			- **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE**: every element of $.message.order.payment['@ondc/org/buyer_app_finder_fee_type'] must be in ["percent", "amount"]
			
			- **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT**: all of the following sub conditions must be met:
			
			  - **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT.1**: $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must be present in the payload
			  - **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT.2**: all elements of $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must follow every regex in ["^(\\d*.?\\d{1,2})$"]
			
			- **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE**: every element of $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must be in ["upi", "neft", "rtgs"]
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must **not** be present in the payload
		
		- **ORDER_PAYMENT_ADDITIONAL_PROPERTIES** : All the following sub conditions must pass as per the api requirement
		
			- **condition PAYMENT_URI**: $.message.order.payment.uri must be present in the payload
			
				> Note: **Condition PAYMENT_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.payment.uri must **not** be present in the payload
			
			- **condition PAYMENT_TL_METHOD**: $.message.order.payment.tl_method must be present in the payload
			
				> Note: **Condition PAYMENT_TL_METHOD** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.payment.tl_method must **not** be present in the payload
			
			- **PAYMENT_PARAMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_CURRENCY**: $.message.order.payment.params.currency must be present in the payload
				
				- **condition PAYMENT_TRANSACTION_ID**: $.message.order.payment.params.transaction_id must be present in the payload
				
					> Note: **Condition PAYMENT_TRANSACTION_ID** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment.params.transaction_id must **not** be present in the payload
				
				- **condition PAYMENT_AMOUNT**: $.message.order.payment.params.amount must be present in the payload
			
			- **condition PAYMENT_STATUS**: all of the following sub conditions must be met:
			
			  - **condition PAYMENT_STATUS.1**: $.message.order.payment.status must be present in the payload
			  - **condition PAYMENT_STATUS.2**: every element of $.message.order.payment.status must be in ["NOT-PAID", "PAID"]
			
			- **condition PAYMENT_TYPE**: all of the following sub conditions must be met:
			
			  - **condition PAYMENT_TYPE.1**: $.message.order.payment.type must be present in the payload
			  - **condition PAYMENT_TYPE.2**: every element of $.message.order.payment.type must be in ["ON-ORDER", "ON-FULFILLMENT"]
			
			- **condition PAYMENT_COLLECTED_BY**: all of the following sub conditions must be met:
			
			  - **condition PAYMENT_COLLECTED_BY.1**: $.message.order.payment.collected_by must be present in the payload
			  - **condition PAYMENT_COLLECTED_BY.2**: every element of $.message.order.payment.collected_by must be in ["BAP", "BPP"]
			
			- **condition PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW**: $.message.order.payment['@ondc/org/settlement_window'] must be present in the payload
			
				> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.payment['@ondc/org/settlement_window'] must **not** be present in the payload
			
			- **condition PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT**: $.message.order.payment['@ondc/org/withholding_amount'] must be present in the payload
			
				> Note: **Condition PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.payment['@ondc/org/withholding_amount'] must **not** be present in the payload
			
			- **condition PAYMENT_ONDC_ORG_SETTLEMENT_BASIS**: all of the following sub conditions must be met:
			
			  - **condition PAYMENT_ONDC_ORG_SETTLEMENT_BASIS.1**: $.message.order.payment['@ondc/org/settlement_basis'] must be present in the payload
			  - **condition PAYMENT_ONDC_ORG_SETTLEMENT_BASIS.2**: every element of $.message.order.payment['@ondc/org/settlement_basis'] must be in ["shipment", "delivery", "return_Window_expiry"]
			
				> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_BASIS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.payment['@ondc/org/settlement_basis'] must **not** be present in the payload
			
			- **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_ADDITIONAL_PROPERTIES** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_reference must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_reference must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_status must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_status must **not** be present in the payload
		
		- **ORDER_DOCUMENTS** : All the following sub conditions must pass as per the api requirement
		
			- **condition DOCUMENTS_URL**: $.message.order.documents[*].url must be present in the payload
			
				> Note: **Condition DOCUMENTS_URL** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.documents[*].url must **not** be present in the payload
			
			- **condition DOCUMENTS_LABEL**: $.message.order.documents[*].label must be present in the payload
			
				> Note: **Condition DOCUMENTS_LABEL** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.documents[*].label must **not** be present in the payload
		
		- **condition ORDER_CREATED_AT**: all of the following sub conditions must be met:
		
		  - **condition ORDER_CREATED_AT.1**: $.message.order.created_at must be present in the payload
		  - **condition ORDER_CREATED_AT.2**: all elements of $.message.order.created_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
		
		- **condition ORDER_UPDATED_AT**: all of the following sub conditions must be met:
		
		  - **condition ORDER_UPDATED_AT.1**: $.message.order.updated_at must be present in the payload
		  - **condition ORDER_UPDATED_AT.2**: all elements of $.message.order.updated_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

- **update** : All the following sub conditions must pass as per the api requirement

	- **UPDATE_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["update"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["update"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["update"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["update"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["update"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["update"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **condition UPDATE_TARGET**: all of the following sub conditions must be met:
	
	  - **condition UPDATE_TARGET.1**: $.message.update_target must be present in the payload
	  - **condition UPDATE_TARGET.2**: every element of $.message.update_target must be in ["payment", "item", "billing", "fulfillment"]
	
	- **UPDATE_ORDER** : All the following sub conditions must pass as per the api requirement
	
		- **condition ORDER_ID**: $.message.order.id must be present in the payload
		
		- **ORDER_FULFILLMENTS** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENTS_ID**: $.message.order.fulfillments[*].id must be present in the payload
			
				> Note: **Condition FULFILLMENTS_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.fulfillments[*].id must **not** be present in the payload
			
			- **condition FULFILLMENTS_TYPE**: $.message.order.fulfillments[*].type must be present in the payload
			
			- **FULFILLMENTS_END** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE**: $.message.order.fulfillments[*].end.instructions.additional_desc.content_type must be present in the payload
				
					> Note: **Condition FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].end.instructions.additional_desc.content_type must **not** be present in the payload
			
			- **FULFILLMENTS_TAGS** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_TAGS_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[*].code must be in ["return_request", "update_state", "cancel_request", "update_fulfillment_time", "update_agent_details", "update_label", "reverseqc_output", "bnp_receivables_claim", "bnp_diff_weight", "bnp_diff_length", "bnp_diff_breadth", "bnp_diff_height", "update_verification", "update_state", "update_fulfillment_delay", "linked_order_diff", "update_sale_invoice", "linked_order_diff_proof"]
				
					> Note: **Condition FULFILLMENTS_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].tags[*].code must **not** be present in the payload
				
				- **TAGS_RETURN_REQUEST** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_RETURN_REQUEST_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[*].code must be in ["id", "item_id", "parent_item_id", "item_quantity", "reason_id", "reason_desc", "images", "ttl_approval", "ttl_reverseqc"]
					
						> Note: **Condition TAGS_RETURN_REQUEST_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[*].code must **not** be present in the payload
					
					- **condition RETURN_REQUEST_ID**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value must be present in the payload
					
						> Note: **Condition RETURN_REQUEST_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_ITEM_ID**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value must be present in the payload
					
						> Note: **Condition RETURN_REQUEST_ITEM_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_PARENT_ITEM_ID**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value must be present in the payload
					
						> Note: **Condition RETURN_REQUEST_PARENT_ITEM_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_ITEM_QUANTITY**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value must be present in the payload
					
						> Note: **Condition RETURN_REQUEST_ITEM_QUANTITY** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_REASON_ID**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value must follow every regex in ["^\\d{3}$"]
					
						> Note: **Condition RETURN_REQUEST_REASON_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_REASON_DESC**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value must be present in the payload
					
						> Note: **Condition RETURN_REQUEST_REASON_DESC** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_IMAGES**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value must be present in the payload
					
						> Note: **Condition RETURN_REQUEST_IMAGES** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_TTL_APPROVAL**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value must follow every regex in ["^PT[0-9]+H$"]
					
						> Note: **Condition RETURN_REQUEST_TTL_APPROVAL** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_TTL_REVERSEQC**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value must follow every regex in ["^P[0-9]+D$"]
					
						> Note: **Condition RETURN_REQUEST_TTL_REVERSEQC** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_STATE** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_STATE_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[*].code must be in ["state", "reason_id"]
					
						> Note: **Condition TAGS_UPDATE_STATE_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[*].code must **not** be present in the payload
					
					- **condition UPDATE_STATE_STATE**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value must be in ["Order-picked-up", "Order-delivered"]
					
						> Note: **Condition UPDATE_STATE_STATE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value must **not** be present in the payload
					
					- **condition UPDATE_STATE_REASON_ID**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value must be present in the payload
					
						> Note: **Condition UPDATE_STATE_REASON_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value must **not** be present in the payload
				
				- **TAGS_CANCEL_REQUEST** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_CANCEL_REQUEST_RETRY_COUNT_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[*].code must be in ["retry_count", "reason_id", "initiated_by"]
					
						> Note: **Condition TAGS_CANCEL_REQUEST_RETRY_COUNT_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[*].code must **not** be present in the payload
					
					- **condition CANCEL_REQUEST_RETRY_COUNT**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value must be present in the payload
					
						> Note: **Condition CANCEL_REQUEST_RETRY_COUNT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value must **not** be present in the payload
					
					- **condition CANCEL_REQUEST_REASON_ID**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value must be present in the payload
					
						> Note: **Condition CANCEL_REQUEST_REASON_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value must **not** be present in the payload
					
					- **condition CANCEL_REQUEST_INITIATED_BY**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value must be present in the payload
					
						> Note: **Condition CANCEL_REQUEST_INITIATED_BY** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_FULFILLMENT_TIME** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_FULFILLMENT_TIME_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[*].code must be in ["state", "timestamp", "start_time", "end_time"]
					
						> Note: **Condition TAGS_UPDATE_FULFILLMENT_TIME_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[*].code must **not** be present in the payload
					
					- **condition UPDATE_FULFILLMENT_TIME_STATE**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value must be in ["Order-picked-up"]
					
						> Note: **Condition UPDATE_FULFILLMENT_TIME_STATE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value must **not** be present in the payload
					
					- **condition UPDATE_FULFILLMENT_TIME_TIMESTAMP**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition UPDATE_FULFILLMENT_TIME_TIMESTAMP** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value must **not** be present in the payload
					
					- **condition UPDATE_FULFILLMENT_TIME_START**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition UPDATE_FULFILLMENT_TIME_START** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value must **not** be present in the payload
					
					- **condition UPDATE_FULFILLMENT_TIME_END**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition UPDATE_FULFILLMENT_TIME_END** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_AGENT_DETAILS** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_AGENT_DETAILS_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[*].code must be in ["name", "phone", "provider_id"]
					
						> Note: **Condition TAGS_UPDATE_AGENT_DETAILS_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[*].code must **not** be present in the payload
					
					- **condition AGENT_NAME**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value must be present in the payload
					
						> Note: **Condition AGENT_NAME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value must **not** be present in the payload
					
					- **condition AGENT_PHONE**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value must be present in the payload
					
						> Note: **Condition AGENT_PHONE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value must **not** be present in the payload
					
					- **condition AGENT_PROVIDER_ID**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value must be present in the payload
					
						> Note: **Condition AGENT_PROVIDER_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_LABEL** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_LABEL_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[*].code must be in ["type", "url", "shipping"]
					
						> Note: **Condition TAGS_UPDATE_LABEL_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[*].code must **not** be present in the payload
					
					- **condition LABEL_TYPE**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value must be in ["webp", "png", "jpeg", "pdf"]
					
						> Note: **Condition LABEL_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value must **not** be present in the payload
					
					- **condition LABEL_URL**: $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value must be present in the payload
					
						> Note: **Condition LABEL_URL** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value must **not** be present in the payload
					
					- **condition LABEL_SHIPPING**: $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value must be present in the payload
					
						> Note: **Condition LABEL_SHIPPING** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value must **not** be present in the payload
				
				- **TAGS_REVERSEQC_OUTPUT** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_REVERSEQC_OUTPUT_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[*].code must be in ["P001", "P003", "Q001"]
					
						> Note: **Condition TAGS_REVERSEQC_OUTPUT_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[*].code must **not** be present in the payload
					
					- **condition RQC_P001**: $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value must be present in the payload
					
						> Note: **Condition RQC_P001** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value must **not** be present in the payload
					
					- **condition RQC_P003**: $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value must be present in the payload
					
						> Note: **Condition RQC_P003** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value must **not** be present in the payload
					
					- **condition RQC_Q001**: every element of $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value must be in ["yes", "no"]
					
						> Note: **Condition RQC_Q001** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value must **not** be present in the payload
				
				- **TAGS_BNP_RECEIVABLES_CLAIM** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_BNP_RECIEVABLES_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[*].code must be in ["type", "currency", "value"]
					
						> Note: **Condition TAGS_BNP_RECIEVABLES_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[*].code must **not** be present in the payload
					
					- **condition CLAIM_TYPE**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value must be present in the payload
					
						> Note: **Condition CLAIM_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value must **not** be present in the payload
					
					- **condition CLAIM_CURRENCY**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value must be present in the payload
					
						> Note: **Condition CLAIM_CURRENCY** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value must **not** be present in the payload
					
					- **condition CLAIM_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition CLAIM_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value must **not** be present in the payload
				
				- **TAGS_BNP_DIFF_WEIGHT** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_BNP_DIFF_WEIGHT_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[*].code must be in ["unit", "value"]
					
						> Note: **Condition TAGS_BNP_DIFF_WEIGHT_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[*].code must **not** be present in the payload
					
					- **condition DIFF_WEIGHT_UNIT**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value must be in ["unit", "dozen", "gram", "kilogram", "tonne", "litre", "millilitre"]
					
						> Note: **Condition DIFF_WEIGHT_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value must **not** be present in the payload
					
					- **condition DIFF_WEIGHT_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition DIFF_WEIGHT_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value must **not** be present in the payload
				
				- **TAGS_BNP_DIFF_LENGTH** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_BNP_DIFF_LENGTH_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[*].code must be in ["unit", "value"]
					
						> Note: **Condition TAGS_BNP_DIFF_LENGTH_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[*].code must **not** be present in the payload
					
					- **condition DIFF_LENGTH_UNIT**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value must be in ["centimeter", "meter"]
					
						> Note: **Condition DIFF_LENGTH_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value must **not** be present in the payload
					
					- **condition DIFF_LENGTH_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition DIFF_LENGTH_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value must **not** be present in the payload
				
				- **TAGS_BNP_DIFF_BREADTH** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_BNP_DIFF_BREADTH_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[*].code must be in ["unit", "value"]
					
						> Note: **Condition TAGS_BNP_DIFF_BREADTH_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[*].code must **not** be present in the payload
					
					- **condition DIFF_BREADTH_UNIT**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value must be present in the payload
					
						> Note: **Condition DIFF_BREADTH_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value must **not** be present in the payload
					
					- **condition DIFF_BREADTH_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition DIFF_BREADTH_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value must **not** be present in the payload
				
				- **TAGS_BNP_DIFF_HEIGHT** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_BNP_DIFF_HEIGHT_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[*].code must be in ["unit", "value"]
					
						> Note: **Condition TAGS_BNP_DIFF_HEIGHT_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[*].code must **not** be present in the payload
					
					- **condition DIFF_HEIGHT_UNIT**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value must be present in the payload
					
						> Note: **Condition DIFF_HEIGHT_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value must **not** be present in the payload
					
					- **condition DIFF_HEIGHT_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition DIFF_HEIGHT_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_VERIFICATION** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_VERIFICATION_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[*].code must be in ["type", "value"]
					
						> Note: **Condition TAGS_UPDATE_VERIFICATION_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[*].code must **not** be present in the payload
					
					- **condition VERIFICATION_TYPE**: $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value must be present in the payload
					
						> Note: **Condition VERIFICATION_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value must **not** be present in the payload
					
					- **condition VERIFICATION_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition VERIFICATION_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_STATE_TIMESTAMPS** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_STATE_TIMESTAMPS_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[*].code must be in ["timestamp", "start_time", "end_time"]
					
						> Note: **Condition TAGS_UPDATE_STATE_TIMESTAMPS_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[*].code must **not** be present in the payload
					
					- **condition STATE_TIMESTAMP**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition STATE_TIMESTAMP** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value must **not** be present in the payload
					
					- **condition STATE_START_TIME**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition STATE_START_TIME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value must **not** be present in the payload
					
					- **condition STATE_END_TIME**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition STATE_END_TIME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_FULFILLMENT_DELAY** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_FULFILLMENT_DELAY_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[*].code must be in ["state", "start_time", "end_time", "reason_id", "attempt"]
					
						> Note: **Condition TAGS_UPDATE_FULFILLMENT_DELAY_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[*].code must **not** be present in the payload
					
					- **condition DELAY_STATE**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value must be in ["Order-picked-up", "Order-delivered"]
					
						> Note: **Condition DELAY_STATE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value must **not** be present in the payload
					
					- **condition DELAY_REASON_ID**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value must be present in the payload
					
						> Note: **Condition DELAY_REASON_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value must **not** be present in the payload
					
					- **condition DELAY_START_TIME**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition DELAY_START_TIME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value must **not** be present in the payload
					
					- **condition DELAY_END_TIME**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition DELAY_END_TIME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value must **not** be present in the payload
					
					- **condition DELAY_ATTEMPT**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value must be in ["yes", "no"]
					
						> Note: **Condition DELAY_ATTEMPT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value must **not** be present in the payload
				
				- **TAGS_LINKED_ORDER_DIFF** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_LINKED_ORDER_DIFF_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[*].code must be in ["id", "weight_unit", "weight_value", "dim_unit", "length", "breadth", "height"]
					
						> Note: **Condition TAGS_LINKED_ORDER_DIFF_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[*].code must **not** be present in the payload
					
					- **condition LINKED_ORDER_ID**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value must be present in the payload
					
						> Note: **Condition LINKED_ORDER_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value must **not** be present in the payload
					
					- **condition LINKED_WEIGHT_UNIT**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value must be present in the payload
					
						> Note: **Condition LINKED_WEIGHT_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value must **not** be present in the payload
					
					- **condition LINKED_WEIGHT_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value must be present in the payload
					
						> Note: **Condition LINKED_WEIGHT_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value must **not** be present in the payload
					
					- **condition LINKED_DIM_UNIT**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value must be present in the payload
					
						> Note: **Condition LINKED_DIM_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value must **not** be present in the payload
					
					- **condition LINKED_LENGTH**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value must be present in the payload
					
						> Note: **Condition LINKED_LENGTH** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value must **not** be present in the payload
					
					- **condition LINKED_BREADTH**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value must be present in the payload
					
						> Note: **Condition LINKED_BREADTH** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value must **not** be present in the payload
					
					- **condition LINKED_HEIGHT**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value must be present in the payload
					
						> Note: **Condition LINKED_HEIGHT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value must **not** be present in the payload
				
				- **TAGS_LINKED_ORDER_DIFF_PROOF** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_LINKED_ORDER_DIFF_PROOF_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[*].code must be in ["type", "url"]
					
						> Note: **Condition TAGS_LINKED_ORDER_DIFF_PROOF_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[*].code must **not** be present in the payload
					
					- **condition PROOF_TYPE**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value must be present in the payload
					
						> Note: **Condition PROOF_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value must **not** be present in the payload
					
					- **condition PROOF_URL**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value must follow every regex in ["^https?://.*$"]
					
						> Note: **Condition PROOF_URL** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value must **not** be present in the payload
				
				- **condition TAGS_UPDATE_SALE_INVOICE_URL**: all of the following sub conditions must be met:
				
				  - **condition TAGS_UPDATE_SALE_INVOICE_URL.1**: $.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value must be present in the payload
				  - **condition TAGS_UPDATE_SALE_INVOICE_URL.2**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value must follow every regex in ["^https?://.*$"]
				
					> Note: **Condition TAGS_UPDATE_SALE_INVOICE_URL** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value must **not** be present in the payload
		
		- **ORDER_PAYMENT** : All the following sub conditions must pass as per the api requirement
		
			- **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE**: every element of $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must be in ["upi", "neft", "rtgs", "wallet", "netbanking", "paylater", "card"]
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp must **not** be present in the payload

- **track** : All the following sub conditions must pass as per the api requirement

	- **TRACK_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["track"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["track"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["track"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["track"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["track"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["track"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **TRACK_ORDER** : All the following sub conditions must pass as per the api requirement
	
		- **condition ORDER_ID**: all of the following sub conditions must be met:
		
		  - **condition ORDER_ID.1**: $.message.order_id must be present in the payload
		  - **condition ORDER_ID.2**: all elements of $.message.order_id must follow every regex in ["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"]

- **on_track** : All the following sub conditions must pass as per the api requirement

	- **ON_TRACK_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_track"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_track"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_track"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["on_track"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_track"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_track"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **ON_TRACK_TRACKING** : All the following sub conditions must pass as per the api requirement
	
		- **condition TRACKING_ID**: $.message.tracking.id must be present in the payload
		
		- **condition TRACKING_STATUS**: all of the following sub conditions must be met:
		
		  - **condition TRACKING_STATUS.1**: $.message.tracking.status must be present in the payload
		  - **condition TRACKING_STATUS.2**: every element of $.message.tracking.status must be in ["active", "inactive"]
		
		- **TRACKING_LOCATION** : All the following sub conditions must pass as per the api requirement
		
			- **condition TRACKING_LOCATION_GPS**: $.message.tracking.location.gps must be present in the payload
			
				> Note: **Condition TRACKING_LOCATION_GPS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.tracking.location.gps must **not** be present in the payload
			
			- **condition TRACKING_LOCATION_TIME_TIMESTAMP**: all elements of $.message.tracking.location.time.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
				> Note: **Condition TRACKING_LOCATION_TIME_TIMESTAMP** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.tracking.location.time.timestamp must **not** be present in the payload
			
			- **condition TRACKING_LOCATION_UPDATED_AT**: all elements of $.message.tracking.location.updated_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
				> Note: **Condition TRACKING_LOCATION_UPDATED_AT** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.tracking.location.updated_at must **not** be present in the payload
		
		- **TRACKING_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **condition TRACKING_VALID_TAGS**: every element of $.message.tracking.tags[*].code must be in ["id", "config", "path"]
			
				> Note: **Condition TRACKING_VALID_TAGS** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.tracking.tags[*].code must **not** be present in the payload
			
			- **TRACKING_ORDER_TAG** : All the following sub conditions must pass as per the api requirement
			
				- **condition ORDER_ID**: $.message.tracking.tags[?(@.code=='order')].list[?(@.code=='id')].value must be present in the payload
				
					> Note: **Condition ORDER_ID** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.tracking.tags[?(@.code=='order')].list[?(@.code=='id')].value must **not** be present in the payload
			
			- **TRACKING_CONFIG_TAG** : All the following sub conditions must pass as per the api requirement
			
				- **condition TRACKING_CONFIG_VALID_TAGS**: every element of $.message.tracking.tags[?(@.code=='config')].list[*].code must be in ["attr", "type"]
				
					> Note: **Condition TRACKING_CONFIG_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.tracking.tags[?(@.code=='config')].list[*].code must **not** be present in the payload
				
				- **condition CONFIG_ATTR**: $.message.tracking.tags[?(@.code=='config')].list[?(@.code=='attr')].value must be present in the payload
				
					> Note: **Condition CONFIG_ATTR** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.tracking.tags[?(@.code=='config')].list[?(@.code=='attr')].value must **not** be present in the payload
				
				- **condition CONFIG_TYPE**: every element of $.message.tracking.tags[?(@.code=='config')].list[?(@.code=='type')].value must be in ["live_poll", "deferred"]
				
					> Note: **Condition CONFIG_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.tracking.tags[?(@.code=='config')].list[?(@.code=='type')].value must **not** be present in the payload
			
			- **TRACKING_PATH_TAG** : All the following sub conditions must pass as per the api requirement
			
				- **condition TRACKING_PATH_VALID_TAGS**: every element of $.message.tracking.tags[?(@.code=='path')].list[*].code must be in ["lat_lng", "sequence"]
				
					> Note: **Condition TRACKING_PATH_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.tracking.tags[?(@.code=='path')].list[*].code must **not** be present in the payload
				
				- **condition PATH_LAT_LNG**: $.message.tracking.tags[?(@.code=='path')].list[?(@.code=='lat_lng')].value must be present in the payload
				
					> Note: **Condition PATH_LAT_LNG** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.tracking.tags[?(@.code=='path')].list[?(@.code=='lat_lng')].value must **not** be present in the payload
				
				- **condition PATH_SEQUENCE**: all of the following sub conditions must be met:
				
				  - **condition PATH_SEQUENCE.1**: $.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value must be present in the payload
				  - **condition PATH_SEQUENCE.2**: every element of $.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value must be in ["1", "2", "3"]
				
					> Note: **Condition PATH_SEQUENCE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value must **not** be present in the payload

- **cancel** : All the following sub conditions must pass as per the api requirement

	- **CANCEL_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["cancel"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["cancel"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["cancel"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["cancel"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["cancel"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["cancel"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **condition CANCEL_ORDER_ID**: $.message.order_id must be present in the payload
	
	- **condition CANCELLATION_REASON_ID**: all of the following sub conditions must be met:
	
	  - **condition CANCELLATION_REASON_ID.1**: $.message.cancellation_reason_id must be present in the payload
	  - **condition CANCELLATION_REASON_ID.2**: every element of $.message.cancellation_reason_id must be in ["001", "002", "003", "004", "005", "006", "009", "010", "011", "013", "014", "016", "017", "018", "020", "998", "999"]
	
	- **CANCEL_DESCRIPTOR** : All the following sub conditions must pass as per the api requirement
	
		- **condition CANCEL_DESCRIPTOR_NAME**: $.message.descriptor.name must be present in the payload
		
			> Note: **Condition CANCEL_DESCRIPTOR_NAME** can be skipped if the following conditions are met:
			>
			> - **condition B**: $.message.descriptor.name must **not** be present in the payload
		
		- **condition CANCEL_DESCRIPTOR_SHORT_DESC**: $.message.descriptor.short_desc must be present in the payload
		
			> Note: **Condition CANCEL_DESCRIPTOR_SHORT_DESC** can be skipped if the following conditions are met:
			>
			> - **condition B**: $.message.descriptor.short_desc must **not** be present in the payload
		
		- **CANCEL_DESCRIPTOR_TAGS** : All the following sub conditions must pass as per the api requirement
		
			- **condition PARAMS_FORCE**: every element of $.message.descriptor.tags[*].code must be in ["params", "cancel_request"]
			
				> Note: **Condition PARAMS_FORCE** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.descriptor.tags[*].code must **not** be present in the payload
			
			- **PARAMS_TAG** : All the following sub conditions must pass as per the api requirement
			
				- **condition PARAMS_VALID_TAGS**: every element of $.message.descriptor.tags[?(@.code=='params')].list[*].code must be in ["force", "ttl_response"]
				
					> Note: **Condition PARAMS_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.descriptor.tags[?(@.code=='params')].list[*].code must **not** be present in the payload
				
				- **condition PARAMS_FORCE**: every element of $.message.descriptor.tags[?(@.code=='params')].list[?(@.code=='force')].value must be in ["yes", "no"]
				
					> Note: **Condition PARAMS_FORCE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.descriptor.tags[?(@.code=='params')].list[?(@.code=='force')].value must **not** be present in the payload
				
				- **condition PARAMS_TTL_RESPONSE**: $.message.descriptor.tags[?(@.code=='params')].list[?(@.code=='ttl_response')].value must be present in the payload
				
					> Note: **Condition PARAMS_TTL_RESPONSE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.descriptor.tags[?(@.code=='params')].list[?(@.code=='ttl_response')].value must **not** be present in the payload
			
			- **CANCEL_REQUEST_TAG** : All the following sub conditions must pass as per the api requirement
			
				- **condition CANCEL_REQUEST_VALID_TAGS**: every element of $.message.descriptor.tags[?(@.code=='cancel_request')].list[*].code must be in ["initiated_by"]
				
					> Note: **Condition CANCEL_REQUEST_VALID_TAGS** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.descriptor.tags[?(@.code=='cancel_request')].list[*].code must **not** be present in the payload
				
				- **condition CANCEL_REQUEST_INITIATED_BY**: $.message.descriptor.tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value must be present in the payload
				
					> Note: **Condition CANCEL_REQUEST_INITIATED_BY** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.descriptor.tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value must **not** be present in the payload

- **on_cancel** : All the following sub conditions must pass as per the api requirement

	- **ON_CANCEL_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_cancel"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_cancel"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_cancel"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["on_cancel"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_cancel"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_cancel"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **ON_CANCEL_ORDER** : All the following sub conditions must pass as per the api requirement
	
		- **condition ORDER_ID**: all of the following sub conditions must be met:
		
		  - **condition ORDER_ID.1**: $.message.order.id must be present in the payload
		  - **condition ORDER_ID.2**: all elements of $.message.order.id must follow every regex in ["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"]
		
		- **condition ORDER_STATE**: every element of $.message.order.state must be in ["Cancelled"]
		
		- **ORDER_CANCELLATION** : All the following sub conditions must pass as per the api requirement
		
			- **condition CANCELLED_BY**: $.message.order.cancellation.cancelled_by must be present in the payload
			
			- **condition CANCELLATION_REASON_ID**: $.message.order.cancellation.reason.id must be present in the payload
		
		- **ORDER_PROVIDER** : All the following sub conditions must pass as per the api requirement
		
			- **condition ORDER_PROVIDER_ID**: $.message.order.provider.id must be present in the payload
			
			- **condition ORDER_PROVIDER_LOCATIONS_ID**: $.message.order.provider.locations[*].id must be present in the payload
		
		- **ORDER_ITEMS** : All the following sub conditions must pass as per the api requirement
		
			- **condition ORDER_ITEM_ID**: all of the following sub conditions must be met:
			
			  - **condition ORDER_ITEM_ID.1**: $.message.order.items[*].id must be present in the payload
			  - **condition ORDER_ITEM_ID.2**: all elements of $.message.order.items[*].id must follow every regex in ["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"]
			
			- **condition ORDER_ITEM_FULFILLMENT_ID**: $.message.order.items[*].fulfillment_id must be present in the payload
			
			- **condition ORDER_ITEM_QUANTITY_COUNT**: $.message.order.items[*].quantity.count must be present in the payload
		
		- **ORDER_BILLING** : All the following sub conditions must pass as per the api requirement
		
			- **BILLING_ADDRESS** : All the following sub conditions must pass as per the api requirement
			
				- **condition BILLING_ADDRESS_NAME**: $.message.order.billing.address.name must be present in the payload
				
				- **condition BILLING_ADDRESS_BUILDING**: $.message.order.billing.address.building must be present in the payload
				
				- **condition BILLING_ADDRESS_LOCALITY**: $.message.order.billing.address.locality must be present in the payload
				
				- **condition BILLING_ADDRESS_CITY**: $.message.order.billing.address.city must be present in the payload
				
				- **condition BILLING_ADDRESS_STATE**: $.message.order.billing.address.state must be present in the payload
				
				- **condition BILLING_ADDRESS_COUNTRY**: $.message.order.billing.address.country must be present in the payload
				
				- **condition BILLING_ADDRESS_AREA_CODE**: $.message.order.billing.address.area_code must be present in the payload
			
			- **condition BILLING_PHONE**: $.message.order.billing.phone must be present in the payload
			
			- **condition BILLING_NAME**: $.message.order.billing.name must be present in the payload
			
			- **condition BILLING_CREATED_AT**: $.message.order.billing.created_at must be present in the payload
			
			- **condition BILLING_UPDATED_AT**: $.message.order.billing.updated_at must be present in the payload
		
		- **ORDER_FULFILLMENTS** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENTS_ID**: $.message.order.fulfillments[*].id must be present in the payload
			
			- **condition FULFILLMENTS_STATE_DESCRIPTOR_CODE**: all of the following sub conditions must be met:
			
			  - **condition FULFILLMENTS_STATE_DESCRIPTOR_CODE.1**: $.message.order.fulfillments[*].state.descriptor.code must be present in the payload
			  - **condition FULFILLMENTS_STATE_DESCRIPTOR_CODE.2**: every element of $.message.order.fulfillments[*].state.descriptor.code must be in ["Cancelled", "RTO-Initiated", "RTO-Disposed", "RTO-Delivered"]
			
			- **condition FULFILLMENTS_TYPE**: $.message.order.fulfillments[*].type must be present in the payload
			
			- **condition FULFILLMENTS_ONDC_ORG_PROVIDER_NAME**: $.message.order.fulfillments[*]['@ondc/org/provider_name'] must be present in the payload
			
				> Note: **Condition FULFILLMENTS_ONDC_ORG_PROVIDER_NAME** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.fulfillments[*]['@ondc/org/provider_name'] must **not** be present in the payload
			
			- **condition FULFILLMENTS_TRACKING**: $.message.order.fulfillments[*].tracking must be present in the payload
			
				> Note: **Condition FULFILLMENTS_TRACKING** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.fulfillments[*].tracking must **not** be present in the payload
			
			- **FULFILLMENTS_START** : All the following sub conditions must pass as per the api requirement
			
				- **FULFILLMENTS_START_LOCATION** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_START_LOCATION_ID**: $.message.order.fulfillments[*].start.location.id must be present in the payload
					
					- **condition FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME**: $.message.order.fulfillments[*].start.location.descriptor.name must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.location.descriptor.name must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_LOCATION_GPS**: $.message.order.fulfillments[*].start.location.gps must be present in the payload
					
					- **FULFILLMENTS_START_LOCATION_ADDRESS** : All the following sub conditions must pass as per the api requirement
					
						- **condition FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY**: $.message.order.fulfillments[*].start.location.address.locality must be present in the payload
						
						- **condition FULFILLMENTS_START_LOCATION_ADDRESS_CITY**: $.message.order.fulfillments[*].start.location.address.city must be present in the payload
						
						- **condition FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE**: $.message.order.fulfillments[*].start.location.address.area_code must be present in the payload
						
						- **condition FULFILLMENTS_START_LOCATION_ADDRESS_STATE**: $.message.order.fulfillments[*].start.location.address.state must be present in the payload
				
				- **FULFILLMENTS_START_TIME** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_START_TIME_RANGE_START**: $.message.order.fulfillments[*].start.time.range.start must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_TIME_RANGE_START** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.time.range.start must **not** be present in the payload
					
					- **condition FULFILLMENTS_START_TIME_RANGE_END**: $.message.order.fulfillments[*].start.time.range.end must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_TIME_RANGE_END** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.time.range.end must **not** be present in the payload
				
				- **FULFILLMENTS_START_CONTACT** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_START_CONTACT_PHONE**: $.message.order.fulfillments[*].start.contact.phone must be present in the payload
					
					- **condition FULFILLMENTS_START_CONTACT_EMAIL**: $.message.order.fulfillments[*].start.contact.email must be present in the payload
					
						> Note: **Condition FULFILLMENTS_START_CONTACT_EMAIL** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].start.contact.email must **not** be present in the payload
			
			- **FULFILLMENTS_END** : All the following sub conditions must pass as per the api requirement
			
				- **FULFILLMENTS_END_LOCATION** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_END_LOCATION_GPS**: $.message.order.fulfillments[*].end.location.gps must be present in the payload
					
					- **FULFILLMENTS_END_LOCATION_ADDRESS** : All the following sub conditions must pass as per the api requirement
					
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_NAME**: $.message.order.fulfillments[*].end.location.address.name must be present in the payload
						
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING**: $.message.order.fulfillments[*].end.location.address.building must be present in the payload
						
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY**: $.message.order.fulfillments[*].end.location.address.locality must be present in the payload
						
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY**: $.message.order.fulfillments[*].end.location.address.country must be present in the payload
						
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_CITY**: $.message.order.fulfillments[*].end.location.address.city must be present in the payload
						
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE**: $.message.order.fulfillments[*].end.location.address.area_code must be present in the payload
						
						- **condition FULFILLMENTS_END_LOCATION_ADDRESS_STATE**: $.message.order.fulfillments[*].end.location.address.state must be present in the payload
				
				- **FULFILLMENTS_END_TIME** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_END_TIME_RANGE_START**: $.message.order.fulfillments[*].end.time.range.start must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_TIME_RANGE_START** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.time.range.start must **not** be present in the payload
					
					- **condition FULFILLMENTS_END_TIME_RANGE_END**: $.message.order.fulfillments[*].end.time.range.end must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_TIME_RANGE_END** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.time.range.end must **not** be present in the payload
				
				- **condition FULFILLMENTS_END_PERSON_NAME**: $.message.order.fulfillments[*].end.person.name must be present in the payload
				
					> Note: **Condition FULFILLMENTS_END_PERSON_NAME** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].end.person.name must **not** be present in the payload
				
				- **FULFILLMENTS_END_CONTACT** : All the following sub conditions must pass as per the api requirement
				
					- **condition FULFILLMENTS_END_CONTACT_PHONE**: $.message.order.fulfillments[*].end.contact.phone must be present in the payload
					
					- **condition FULFILLMENTS_END_CONTACT_EMAIL**: $.message.order.fulfillments[*].end.contact.email must be present in the payload
					
						> Note: **Condition FULFILLMENTS_END_CONTACT_EMAIL** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].end.contact.email must **not** be present in the payload
			
			- **FULFILLMENTS_TAGS** : All the following sub conditions must pass as per the api requirement
			
				- **condition CANCEL_REQUEST_ID**: $.message.order.tags[*].code must be present in the payload
				
					> Note: **Condition CANCEL_REQUEST_ID** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.tags[*].code must **not** be present in the payload
				
				- **TAGS_CANCEL_REQUEST** : All the following sub conditions must pass as per the api requirement
				
					- **condition CANCEL_REQUEST_VALID_TAGS**: every element of $.message.order.tags[?(@.code=='cancel_request')].list[*].code must be in ["id", "reason_id", "initiated_by", "retry_count", "rto_id"]
					
						> Note: **Condition CANCEL_REQUEST_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='cancel_request')].list[*].code must **not** be present in the payload
					
					- **condition CANCEL_REQUEST_ID**: $.message.order.tags[?(@.code=='cancel_request')].list[?(@.code=='id')].value must be present in the payload
					
						> Note: **Condition CANCEL_REQUEST_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='cancel_request')].list[?(@.code=='id')].value must **not** be present in the payload
					
					- **condition CANCEL_REQUEST_REASON_ID**: $.message.order.tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value must be present in the payload
					
						> Note: **Condition CANCEL_REQUEST_REASON_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value must **not** be present in the payload
					
					- **condition CANCEL_REQUEST_INITIATED_BY**: $.message.order.tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value must be present in the payload
					
						> Note: **Condition CANCEL_REQUEST_INITIATED_BY** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value must **not** be present in the payload
					
					- **condition CANCEL_REQUEST_RETRY_COUNT**: $.message.order.tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value must be present in the payload
					
						> Note: **Condition CANCEL_REQUEST_RETRY_COUNT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value must **not** be present in the payload
					
					- **condition CANCEL_REQUEST_RTO_ID**: $.message.order.tags[?(@.code=='cancel_request')].list[?(@.code=='rto_id')].value must be present in the payload
					
						> Note: **Condition CANCEL_REQUEST_RTO_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='cancel_request')].list[?(@.code=='rto_id')].value must **not** be present in the payload
				
				- **TAGS_IGM_REQUEST** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_IGM_REQUEST_VALID_TAGS**: every element of $.message.order.tags[?(@.code=='igm_request')].list[*].code must be in ["id"]
					
						> Note: **Condition TAGS_IGM_REQUEST_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='igm_request')].list[*].code must **not** be present in the payload
					
					- **condition IGM_REQUEST_ID**: $.message.order.tags[?(@.code=='igm_request')].list[?(@.code=='id')].value must be present in the payload
					
						> Note: **Condition IGM_REQUEST_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='igm_request')].list[?(@.code=='id')].value must **not** be present in the payload
				
				- **TAGS_PRE_CANCEL_STATE** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_PRE_CANCEL_STATE_VALID_TAGS**: every element of $.message.order.tags[?(@.code=='pre_cancel_state')].list[*].code must be in ["fulfillment_state", "updated_at"]
					
						> Note: **Condition TAGS_PRE_CANCEL_STATE_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='pre_cancel_state')].list[*].code must **not** be present in the payload
					
					- **condition PRE_CANCEL_FULFILLMENT_STATE**: all of the following sub conditions must be met:
					
					  - **condition PRE_CANCEL_FULFILLMENT_STATE.1**: $.message.order.tags[?(@.code=='pre_cancel_state')].list[?(@.code=='fulfillment_state')].value must be present in the payload
					  - **condition PRE_CANCEL_FULFILLMENT_STATE.2**: every element of $.message.order.tags[?(@.code=='pre_cancel_state')].list[?(@.code=='fulfillment_state')].value must be in ["cancelled", "pending"]
					
						> Note: **Condition PRE_CANCEL_FULFILLMENT_STATE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='pre_cancel_state')].list[?(@.code=='fulfillment_state')].value must **not** be present in the payload
					
					- **condition PRE_CANCEL_UPDATED_AT**: all of the following sub conditions must be met:
					
					  - **condition PRE_CANCEL_UPDATED_AT.1**: $.message.order.tags[?(@.code=='pre_cancel_state')].list[?(@.code=='updated_at')].value must be present in the payload
					  - **condition PRE_CANCEL_UPDATED_AT.2**: all elements of $.message.order.tags[?(@.code=='pre_cancel_state')].list[?(@.code=='updated_at')].value must follow every regex in ["^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"]
					
						> Note: **Condition PRE_CANCEL_UPDATED_AT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='pre_cancel_state')].list[?(@.code=='updated_at')].value must **not** be present in the payload
				
				- **TAGS_QUOTE_TRAIL** : All the following sub conditions must pass as per the api requirement
				
					- **condition QUOTE_TRAIL_TYPE_VALID_TAGS**: every element of $.message.order.tags[?(@.code=='quote_trail')].list[*].code must be in ["type", "id", "currency", "value"]
					
						> Note: **Condition QUOTE_TRAIL_TYPE_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='quote_trail')].list[*].code must **not** be present in the payload
					
					- **condition QUOTE_TRAIL_TYPE**: $.message.order.tags[?(@.code=='quote_trail')].list[?(@.code=='type')].value must be present in the payload
					
						> Note: **Condition QUOTE_TRAIL_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='quote_trail')].list[?(@.code=='type')].value must **not** be present in the payload
					
					- **condition QUOTE_TRAIL_ID**: $.message.order.tags[?(@.code=='quote_trail')].list[?(@.code=='id')].value must be present in the payload
					
						> Note: **Condition QUOTE_TRAIL_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='quote_trail')].list[?(@.code=='id')].value must **not** be present in the payload
					
					- **condition QUOTE_TRAIL_CURRENCY**: $.message.order.tags[?(@.code=='quote_trail')].list[?(@.code=='currency')].value must be present in the payload
					
						> Note: **Condition QUOTE_TRAIL_CURRENCY** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='quote_trail')].list[?(@.code=='currency')].value must **not** be present in the payload
					
					- **condition QUOTE_TRAIL_VALUE**: $.message.order.tags[?(@.code=='quote_trail')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition QUOTE_TRAIL_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.tags[?(@.code=='quote_trail')].list[?(@.code=='value')].value must **not** be present in the payload
		
		- **ORDER_QUOTE** : All the following sub conditions must pass as per the api requirement
		
			- **condition QUOTE_PRICE_CURRENCY**: $.message.order.quote.price.currency must be present in the payload
			
			- **condition QUOTE_PRICE_VALUE**: $.message.order.quote.price.value must be present in the payload
			
			- **QUOTE_BREAKUP** : All the following sub conditions must pass as per the api requirement
			
				- **BREAKUP_ITEM** : All the following sub conditions must pass as per the api requirement
				
					- **condition BREAKUP_ITEM_ID**: $.message.order.quote.breakup[*]['@ondc/org/item_id'] must be present in the payload
					
					- **condition BREAKUP_ITEM_QUANTITY_COUNT**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must be present in the payload
					
						> Note: **Condition BREAKUP_ITEM_QUANTITY_COUNT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must **not** be present in the payload
					
					- **condition BREAKUP_ITEM_TITLE_TYPE**: every element of $.message.order.quote.breakup[*]['@ondc/org/title_type'] must be in ["item", "delivery", "packing", "tax", "misc", "discount", "offer"]
					
					- **condition BREAKUP_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].price.currency must be present in the payload
					
					- **condition BREAKUP_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].price.value must be present in the payload
					
					- **BREAKUP_ITEM_ITEM** : All the following sub conditions must pass as per the api requirement
					
						- **condition BREAKUP_ITEM_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].item.price.currency must be present in the payload
						
							> Note: **Condition BREAKUP_ITEM_ITEM_PRICE_CURRENCY** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.quote.breakup[*].item.price.currency must **not** be present in the payload
						
						- **condition BREAKUP_ITEM_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].item.price.value must be present in the payload
						
							> Note: **Condition BREAKUP_ITEM_ITEM_PRICE_VALUE** can be skipped if the following conditions are met:
							>
							> - **condition B**: $.message.order.quote.breakup[*].item.price.value must **not** be present in the payload
						
						- **BREAKUP_ITEM_ITEM_TAGS** : All the following sub conditions must pass as per the api requirement
						
							- **BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE** : All the following sub conditions must pass as per the api requirement
							
								- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must be in ["fulfillment", "order", "item"]
								
									> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE** can be skipped if the following conditions are met:
									>
									> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must **not** be present in the payload
			
			- **condition QUOTE_TTL**: $.message.order.quote.ttl must be present in the payload
		
		- **ORDER_PAYMENT** : All the following sub conditions must pass as per the api requirement
		
			- **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE**: every element of $.message.order.payment['@ondc/org/buyer_app_finder_fee_type'] must be in ["percent", "amount"]
			
			- **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT**: all of the following sub conditions must be met:
			
			  - **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT.1**: $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must be present in the payload
			  - **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT.2**: all elements of $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must follow every regex in ["^(\\d*.?\\d{1,2})$"]
			
			- **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE**: every element of $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must be in ["upi", "neft", "rtgs"]
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must **not** be present in the payload
		
		- **ORDER_PAYMENT_ADDITIONAL_PROPERTIES** : All the following sub conditions must pass as per the api requirement
		
			- **condition PAYMENT_URI**: $.message.order.payment.uri must be present in the payload
			
				> Note: **Condition PAYMENT_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.payment.uri must **not** be present in the payload
			
			- **condition PAYMENT_TL_METHOD**: $.message.order.payment.tl_method must be present in the payload
			
				> Note: **Condition PAYMENT_TL_METHOD** can be skipped if the following conditions are met:
				>
				> - **condition B**: $.message.order.payment.tl_method must **not** be present in the payload
			
			- **PAYMENT_PARAMS** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_CURRENCY**: $.message.order.payment.params.currency must be present in the payload
				
				- **condition PAYMENT_TRANSACTION_ID**: $.message.order.payment.params.transaction_id must be present in the payload
				
					> Note: **Condition PAYMENT_TRANSACTION_ID** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment.params.transaction_id must **not** be present in the payload
				
				- **condition PAYMENT_AMOUNT**: $.message.order.payment.params.amount must be present in the payload
			
			- **condition PAYMENT_STATUS**: all of the following sub conditions must be met:
			
			  - **condition PAYMENT_STATUS.1**: $.message.order.payment.status must be present in the payload
			  - **condition PAYMENT_STATUS.2**: every element of $.message.order.payment.status must be in ["NOT-PAID", "PAID"]
			
			- **condition PAYMENT_TYPE**: all of the following sub conditions must be met:
			
			  - **condition PAYMENT_TYPE.1**: $.message.order.payment.type must be present in the payload
			  - **condition PAYMENT_TYPE.2**: every element of $.message.order.payment.type must be in ["ON-ORDER", "ON-FULFILLMENT"]
			
			- **condition PAYMENT_COLLECTED_BY**: all of the following sub conditions must be met:
			
			  - **condition PAYMENT_COLLECTED_BY.1**: $.message.order.payment.collected_by must be present in the payload
			  - **condition PAYMENT_COLLECTED_BY.2**: every element of $.message.order.payment.collected_by must be in ["BAP", "BPP"]
		
		- **condition ORDER_CREATED_AT**: all of the following sub conditions must be met:
		
		  - **condition ORDER_CREATED_AT.1**: $.message.order.created_at must be present in the payload
		  - **condition ORDER_CREATED_AT.2**: all elements of $.message.order.created_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
		
		- **condition ORDER_UPDATED_AT**: all of the following sub conditions must be met:
		
		  - **condition ORDER_UPDATED_AT.1**: $.message.order.updated_at must be present in the payload
		  - **condition ORDER_UPDATED_AT.2**: all elements of $.message.order.updated_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

- **on_update** : All the following sub conditions must pass as per the api requirement

	- **ON_UPDATE_CONTEXT** : All the following sub conditions must pass as per the api requirement
	
		- **CONTEXT_REQUIRED** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload
			
			- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload
			
			- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload
			
			- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]
			
			- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload
			
			- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_update"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_update"] must be equal to ["search"]
			
			- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload
			
			- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
			
			- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload
			
				> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_update"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
		
		- **CONTEXT_ENUM** : All the following sub conditions must pass as per the api requirement
		
			- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]
			
			- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["on_update"]
			
			- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5", "1.2.0"]
			
			- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]
			
			- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]
			
				> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
				>
				> - **condition B**: ["on_update"] must be equal to ["search"]
			
			- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
			
				> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
				>
				> - **condition B**: every element of ["on_update"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]
	
	- **ON_UPDATE_ORDER** : All the following sub conditions must pass as per the api requirement
	
		- **condition ORDER_ID**: $.message.order.id must be present in the payload
		
		- **ORDER_FULFILLMENTS** : All the following sub conditions must pass as per the api requirement
		
			- **condition FULFILLMENTS_ID**: $.message.order.fulfillments[*].id must be present in the payload
			
			- **condition FULFILLMENTS_TYPE**: $.message.order.fulfillments[*].type must be present in the payload
			
			- **FULFILLMENTS_END** : All the following sub conditions must pass as per the api requirement
			
				- **condition FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE**: $.message.order.fulfillments[*].end.instructions.additional_desc.content_type must be present in the payload
				
					> Note: **Condition FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].end.instructions.additional_desc.content_type must **not** be present in the payload
			
			- **FULFILLMENTS_TAGS** : All the following sub conditions must pass as per the api requirement
			
				- **condition RETURN_REQUEST_ID**: $.message.order.fulfillments[*].tags[*].code must be present in the payload
				
					> Note: **Condition RETURN_REQUEST_ID** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].tags[*].code must **not** be present in the payload
				
				- **TAGS_RETURN_REQUEST** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_RETURN_REQUEST_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[*].code must be in ["id", "item_id", "parent_item_id", "item_quantity", "reason_id", "reason_desc", "images", "ttl_approval", "ttl_reverseqc", "initiated_by"]
					
						> Note: **Condition TAGS_RETURN_REQUEST_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[*].code must **not** be present in the payload
					
					- **condition RETURN_REQUEST_ID**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value must be present in the payload
					
						> Note: **Condition RETURN_REQUEST_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_ITEM_ID**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value must be present in the payload
					
						> Note: **Condition RETURN_REQUEST_ITEM_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_PARENT_ITEM_ID**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value must be present in the payload
					
						> Note: **Condition RETURN_REQUEST_PARENT_ITEM_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_ITEM_QUANTITY**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value must be present in the payload
					
						> Note: **Condition RETURN_REQUEST_ITEM_QUANTITY** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_REASON_ID**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value must follow every regex in ["^\\d{3}$"]
					
						> Note: **Condition RETURN_REQUEST_REASON_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_REASON_DESC**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value must be present in the payload
					
						> Note: **Condition RETURN_REQUEST_REASON_DESC** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_IMAGES**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value must be present in the payload
					
						> Note: **Condition RETURN_REQUEST_IMAGES** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_TTL_APPROVAL**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value must follow every regex in ["^PT[0-9]+H$"]
					
						> Note: **Condition RETURN_REQUEST_TTL_APPROVAL** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value must **not** be present in the payload
					
					- **condition RETURN_REQUEST_TTL_REVERSEQC**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value must follow every regex in ["^P[0-9]+D$"]
					
						> Note: **Condition RETURN_REQUEST_TTL_REVERSEQC** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_STATE** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_STATE_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[*].code must be in ["state", "reason_id"]
					
						> Note: **Condition TAGS_UPDATE_STATE_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[*].code must **not** be present in the payload
					
					- **condition UPDATE_STATE_STATE**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value must be in ["Order-picked-up", "Order-delivered"]
					
						> Note: **Condition UPDATE_STATE_STATE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value must **not** be present in the payload
					
					- **condition UPDATE_STATE_REASON_ID**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value must be present in the payload
					
						> Note: **Condition UPDATE_STATE_REASON_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value must **not** be present in the payload
				
				- **TAGS_CANCEL_REQUEST** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_CANCEL_REQUEST_RETRY_COUNT_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[*].code must be in ["retry_count", "reason_id", "initiated_by"]
					
						> Note: **Condition TAGS_CANCEL_REQUEST_RETRY_COUNT_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[*].code must **not** be present in the payload
					
					- **condition CANCEL_REQUEST_RETRY_COUNT**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value must be present in the payload
					
						> Note: **Condition CANCEL_REQUEST_RETRY_COUNT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value must **not** be present in the payload
					
					- **condition CANCEL_REQUEST_REASON_ID**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value must be present in the payload
					
						> Note: **Condition CANCEL_REQUEST_REASON_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value must **not** be present in the payload
					
					- **condition CANCEL_REQUEST_INITIATED_BY**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value must be present in the payload
					
						> Note: **Condition CANCEL_REQUEST_INITIATED_BY** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_FULFILLMENT_TIME** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_FULFILLMENT_TIME_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[*].code must be in ["state", "timestamp", "start_time", "end_time"]
					
						> Note: **Condition TAGS_UPDATE_FULFILLMENT_TIME_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[*].code must **not** be present in the payload
					
					- **condition UPDATE_FULFILLMENT_TIME_STATE**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value must be in ["Order-picked-up"]
					
						> Note: **Condition UPDATE_FULFILLMENT_TIME_STATE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value must **not** be present in the payload
					
					- **condition UPDATE_FULFILLMENT_TIME_TIMESTAMP**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition UPDATE_FULFILLMENT_TIME_TIMESTAMP** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value must **not** be present in the payload
					
					- **condition UPDATE_FULFILLMENT_TIME_START**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition UPDATE_FULFILLMENT_TIME_START** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value must **not** be present in the payload
					
					- **condition UPDATE_FULFILLMENT_TIME_END**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition UPDATE_FULFILLMENT_TIME_END** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_AGENT_DETAILS** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_AGENT_DETAILS_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[*].code must be in ["name", "phone", "provider_id", "end_time"]
					
						> Note: **Condition TAGS_UPDATE_AGENT_DETAILS_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[*].code must **not** be present in the payload
					
					- **condition AGENT_NAME**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value must be present in the payload
					
						> Note: **Condition AGENT_NAME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value must **not** be present in the payload
					
					- **condition AGENT_PHONE**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value must be present in the payload
					
						> Note: **Condition AGENT_PHONE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value must **not** be present in the payload
					
					- **condition AGENT_PROVIDER_ID**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value must be present in the payload
					
						> Note: **Condition AGENT_PROVIDER_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_LABEL** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_LABEL_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[*].code must be in ["type", "url", "shipping"]
					
						> Note: **Condition TAGS_UPDATE_LABEL_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[*].code must **not** be present in the payload
					
					- **condition LABEL_TYPE**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value must be in ["webp", "png", "jpeg", "pdf"]
					
						> Note: **Condition LABEL_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value must **not** be present in the payload
					
					- **condition LABEL_URL**: $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value must be present in the payload
					
						> Note: **Condition LABEL_URL** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value must **not** be present in the payload
					
					- **condition LABEL_SHIPPING**: $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value must be present in the payload
					
						> Note: **Condition LABEL_SHIPPING** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value must **not** be present in the payload
				
				- **TAGS_REVERSEQC_OUTPUT** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_REVERSEQC_OUTPUT_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[*].code must be in ["P001", "P003", "Q001"]
					
						> Note: **Condition TAGS_REVERSEQC_OUTPUT_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[*].code must **not** be present in the payload
					
					- **condition RQC_P001**: $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value must be present in the payload
					
						> Note: **Condition RQC_P001** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value must **not** be present in the payload
					
					- **condition RQC_P003**: $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value must be present in the payload
					
						> Note: **Condition RQC_P003** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value must **not** be present in the payload
					
					- **condition RQC_Q001**: every element of $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value must be in ["yes", "no"]
					
						> Note: **Condition RQC_Q001** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value must **not** be present in the payload
				
				- **TAGS_BNP_RECEIVABLES_CLAIM** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_BNP_RECIEVABLES_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[*].code must be in ["type", "currency", "value"]
					
						> Note: **Condition TAGS_BNP_RECIEVABLES_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[*].code must **not** be present in the payload
					
					- **condition CLAIM_TYPE**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value must be present in the payload
					
						> Note: **Condition CLAIM_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value must **not** be present in the payload
					
					- **condition CLAIM_CURRENCY**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value must be present in the payload
					
						> Note: **Condition CLAIM_CURRENCY** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value must **not** be present in the payload
					
					- **condition CLAIM_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition CLAIM_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value must **not** be present in the payload
				
				- **TAGS_BNP_DIFF_WEIGHT** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_BNP_DIFF_WEIGHT_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[*].code must be in ["unit", "value"]
					
						> Note: **Condition TAGS_BNP_DIFF_WEIGHT_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[*].code must **not** be present in the payload
					
					- **condition DIFF_WEIGHT_UNIT**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value must be in ["unit", "dozen", "gram", "kilogram", "tonne", "litre", "millilitre"]
					
						> Note: **Condition DIFF_WEIGHT_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value must **not** be present in the payload
					
					- **condition DIFF_WEIGHT_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition DIFF_WEIGHT_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value must **not** be present in the payload
				
				- **TAGS_BNP_DIFF_LENGTH** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_BNP_DIFF_LENGTH_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[*].code must be in ["unit", "value"]
					
						> Note: **Condition TAGS_BNP_DIFF_LENGTH_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[*].code must **not** be present in the payload
					
					- **condition DIFF_LENGTH_UNIT**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value must be in ["centimeter", "meter"]
					
						> Note: **Condition DIFF_LENGTH_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value must **not** be present in the payload
					
					- **condition DIFF_LENGTH_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition DIFF_LENGTH_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value must **not** be present in the payload
				
				- **TAGS_BNP_DIFF_BREADTH** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_BNP_DIFF_BREADTH_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[*].code must be in ["unit", "value"]
					
						> Note: **Condition TAGS_BNP_DIFF_BREADTH_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[*].code must **not** be present in the payload
					
					- **condition DIFF_BREADTH_UNIT**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value must be present in the payload
					
						> Note: **Condition DIFF_BREADTH_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value must **not** be present in the payload
					
					- **condition DIFF_BREADTH_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition DIFF_BREADTH_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value must **not** be present in the payload
				
				- **TAGS_BNP_DIFF_HEIGHT** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_BNP_DIFF_HEIGHT_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[*].code must be in ["unit", "value"]
					
						> Note: **Condition TAGS_BNP_DIFF_HEIGHT_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[*].code must **not** be present in the payload
					
					- **condition DIFF_HEIGHT_UNIT**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value must be present in the payload
					
						> Note: **Condition DIFF_HEIGHT_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value must **not** be present in the payload
					
					- **condition DIFF_HEIGHT_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition DIFF_HEIGHT_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_VERIFICATION** : All the following sub conditions must pass as per the api requirement
				
					- **condition VERIFICATION_TYPE**: $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value must be present in the payload
					
						> Note: **Condition VERIFICATION_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value must **not** be present in the payload
					
					- **condition VERIFICATION_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value must be present in the payload
					
						> Note: **Condition VERIFICATION_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_STATE_TIMESTAMPS** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_STATE_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[*].code must be in ["state", "reason_id"]
					
						> Note: **Condition TAGS_UPDATE_STATE_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[*].code must **not** be present in the payload
					
					- **condition STATE_TIMESTAMP**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition STATE_TIMESTAMP** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value must **not** be present in the payload
					
					- **condition STATE_START_TIME**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition STATE_START_TIME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value must **not** be present in the payload
					
					- **condition STATE_END_TIME**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition STATE_END_TIME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value must **not** be present in the payload
				
				- **TAGS_UPDATE_FULFILLMENT_DELAY** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_UPDATE_FULFILLMENT_DELAY_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[*].code must be in ["state", "start_time", "end_time", "reason_id", "attempt"]
					
						> Note: **Condition TAGS_UPDATE_FULFILLMENT_DELAY_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[*].code must **not** be present in the payload
					
					- **condition DELAY_STATE**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value must be in ["Order-picked-up", "Order-delivered"]
					
						> Note: **Condition DELAY_STATE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value must **not** be present in the payload
					
					- **condition DELAY_REASON_ID**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value must be present in the payload
					
						> Note: **Condition DELAY_REASON_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value must **not** be present in the payload
					
					- **condition DELAY_START_TIME**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition DELAY_START_TIME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value must **not** be present in the payload
					
					- **condition DELAY_END_TIME**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]
					
						> Note: **Condition DELAY_END_TIME** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value must **not** be present in the payload
					
					- **condition DELAY_ATTEMPT**: every element of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value must be in ["yes", "no"]
					
						> Note: **Condition DELAY_ATTEMPT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value must **not** be present in the payload
				
				- **TAGS_LINKED_ORDER_DIFF** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_LINKED_ORDER_DIFF_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[*].code must be in ["id", "weight_unit", "weight_value", "dim_unit", "length", "breadth", "height"]
					
						> Note: **Condition TAGS_LINKED_ORDER_DIFF_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[*].code must **not** be present in the payload
					
					- **condition LINKED_ORDER_ID**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value must be present in the payload
					
						> Note: **Condition LINKED_ORDER_ID** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value must **not** be present in the payload
					
					- **condition LINKED_WEIGHT_UNIT**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value must be present in the payload
					
						> Note: **Condition LINKED_WEIGHT_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value must **not** be present in the payload
					
					- **condition LINKED_WEIGHT_VALUE**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value must be present in the payload
					
						> Note: **Condition LINKED_WEIGHT_VALUE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value must **not** be present in the payload
					
					- **condition LINKED_DIM_UNIT**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value must be present in the payload
					
						> Note: **Condition LINKED_DIM_UNIT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value must **not** be present in the payload
					
					- **condition LINKED_LENGTH**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value must be present in the payload
					
						> Note: **Condition LINKED_LENGTH** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value must **not** be present in the payload
					
					- **condition LINKED_BREADTH**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value must be present in the payload
					
						> Note: **Condition LINKED_BREADTH** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value must **not** be present in the payload
					
					- **condition LINKED_HEIGHT**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value must be present in the payload
					
						> Note: **Condition LINKED_HEIGHT** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value must **not** be present in the payload
				
				- **TAGS_LINKED_ORDER_DIFF_PROOF** : All the following sub conditions must pass as per the api requirement
				
					- **condition TAGS_LINKED_ORDER_DIFF_PROOF_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[*].code must be in ["type", "url"]
					
						> Note: **Condition TAGS_LINKED_ORDER_DIFF_PROOF_VALID_TAGS** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[*].code must **not** be present in the payload
					
					- **condition PROOF_TYPE**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value must be present in the payload
					
						> Note: **Condition PROOF_TYPE** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value must **not** be present in the payload
					
					- **condition PROOF_URL**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value must follow every regex in ["^https?://.*$"]
					
						> Note: **Condition PROOF_URL** can be skipped if the following conditions are met:
						>
						> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value must **not** be present in the payload
				
				- **condition TAGS_UPDATE_SALE_INVOICE_URL**: all of the following sub conditions must be met:
				
				  - **condition TAGS_UPDATE_SALE_INVOICE_URL.1**: $.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value must be present in the payload
				  - **condition TAGS_UPDATE_SALE_INVOICE_URL.2**: all elements of $.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value must follow every regex in ["^https?://.*$"]
				
					> Note: **Condition TAGS_UPDATE_SALE_INVOICE_URL** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value must **not** be present in the payload
		
		- **ORDER_PAYMENT** : All the following sub conditions must pass as per the api requirement
		
			- **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS** : All the following sub conditions must pass as per the api requirement
			
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE**: every element of $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must be in ["upi", "neft", "rtgs", "wallet", "netbanking", "paylater", "card"]
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount must **not** be present in the payload
				
				- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp must be present in the payload
				
					> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP** can be skipped if the following conditions are met:
					>
					> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp must **not** be present in the payload