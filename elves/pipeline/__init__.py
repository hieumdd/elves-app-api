from elves.pipeline import analytics, items

pipelines = {
    i.name: i
    for i in [
        module.pipeline
        for module in [
            analytics,
            items,
        ]
    ]
}
