<?php
declare(strict_types=1);

// NoticeRedundancyScale SDK base feature

class NoticeRedundancyScaleBaseFeature
{
    public string $version;
    public string $name;
    public bool $active;

    // Positions this feature when added via the client `extend` option:
    // "__before__" / "__after__" / "__replace__" name an already-added
    // feature (mirrors the ts feature `_options`). Declared so setting it
    // on an extension instance avoids the dynamic-property deprecation.
    public ?array $_options = null;

    public function __construct()
    {
        $this->version = '0.0.1';
        $this->name = 'base';
        $this->active = true;
    }

    public function get_version(): string { return $this->version; }
    public function get_name(): string { return $this->name; }
    public function get_active(): bool { return $this->active; }

    public function init(NoticeRedundancyScaleContext $ctx, array $options): void {}
    public function PostConstruct(NoticeRedundancyScaleContext $ctx): void {}
    public function PostConstructEntity(NoticeRedundancyScaleContext $ctx): void {}
    public function SetData(NoticeRedundancyScaleContext $ctx): void {}
    public function GetData(NoticeRedundancyScaleContext $ctx): void {}
    public function GetMatch(NoticeRedundancyScaleContext $ctx): void {}
    public function SetMatch(NoticeRedundancyScaleContext $ctx): void {}
    public function PrePoint(NoticeRedundancyScaleContext $ctx): void {}
    public function PreSpec(NoticeRedundancyScaleContext $ctx): void {}
    public function PreRequest(NoticeRedundancyScaleContext $ctx): void {}
    public function PreResponse(NoticeRedundancyScaleContext $ctx): void {}
    public function PreResult(NoticeRedundancyScaleContext $ctx): void {}
    public function PreDone(NoticeRedundancyScaleContext $ctx): void {}
    public function PreUnexpected(NoticeRedundancyScaleContext $ctx): void {}
}
