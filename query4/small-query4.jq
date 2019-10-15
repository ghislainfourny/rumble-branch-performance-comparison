for $o in json-file("../confusion-2014-03-02/confusion500k.json", 100)
let $t := $o.target
let $g := $o.guess
where $t eq $g
order by $t, $o.country descending, $o.date descending
return $o