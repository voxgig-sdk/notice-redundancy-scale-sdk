<?php
declare(strict_types=1);

// NoticeRedundancyScale SDK utility: make_context

require_once __DIR__ . '/../core/Context.php';

class NoticeRedundancyScaleMakeContext
{
    public static function call(array $ctxmap, ?NoticeRedundancyScaleContext $basectx): NoticeRedundancyScaleContext
    {
        return new NoticeRedundancyScaleContext($ctxmap, $basectx);
    }
}
