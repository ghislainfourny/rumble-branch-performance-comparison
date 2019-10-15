for $o in json-file("../confusion-2014-03-02/confusion500k.json", 100)
group by $c := $o.country, $l := $o.target
return {
    "country" : $c,
    "language" : $l,
    "count": count($o)
}
